# coding:utf-8
import traceback
import os
import sys
# import logging
import io
from os.path import dirname
from info import etl
from config import config_list

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

father_path = dirname(dirname(os.path.abspath(dirname(__file__))))
base_path = dirname(dirname(os.path.abspath(dirname(__file__))))
path = dirname(os.path.abspath(dirname(__file__)))
sys.path.append(path)
sys.path.append(base_path)
sys.path.append(father_path)


# logger = logging.getLogger(__name__)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)


class Extract(object):
	def __init__(self, tab_out, tab_in, col_out, col_in, db_out='tyc', db_in='spider_dim', conn_out=etl, conn_in=etl,
	             num=100000):
		"""

		:param tab_out: 查询表
		:param tab_in: 插入表
		:param col_out: 查询字段
		:param col_in: 插入字段
		:param db_out:
		:param db_in:
		:param conn_out:
		:param conn_in:
		:param num: sql分页步长
		"""
		self.conn_out = conn_out
		self.conn_in = conn_in
		self.cur_out = self.conn_out.cursor()
		self.cur_in = self.conn_in.cursor()
		self.db_out = db_out
		self.db_in = db_in
		self.tab_out = tab_out
		self.tab_in = tab_in
		self.col_out = col_out
		self.col_out_list = self.col_out.split(',')
		self.col_out_num = len(self.col_out_list)
		self.col_in = col_in
		self.num = num
		self.col_list = self.col_in.replace('(', '').replace(')', '').split(',')
		# self.col_list = self._get_column()[1:-1]  # 直接用给定表返回字段列表，这里不用此方式
		# self.col_str = ','.join(self.col_list)  # 对于插入表不用给出字段名，但是为确保兼容性，这里采用给出的方式
		self.val_str = self._handle_str(len(self.col_list))

	# def _get_column(self):
	# 	sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{tab}' and table_schema = '{db}'""".format(
	# 		tab=self.tab_in, db=self.db_in)
	# 	try:
	# 		self.cur.execute(sql)
	# 	except Exception as e:
	# 		print(e)
	# 		print('获取数据表字段错误....')
	# 		exit(1)
	# 	results = self.cur.fetchall()
	# 	col_str = results[0]['group_concat(column_name)']
	# 	col_list = col_str.split(',')
	# 	return col_list

	def _handle_str(self, num):
		"""
		组合sql语句中的values （%s， %s...）字符串
		:param num:
		:return:
		"""
		x = "%s"
		y = ", %s"
		for i in range(num - 1):
			x += y
		return x

	def selectFun(self, start=0):
		"""
		查询函数
		:param start:
		:return:
		"""
		sql = """select {col} from {db}.{tab} limit {start}, {num}""".format(
			col=self.col_out, db=self.db_out, tab=self.tab_out, start=start, num=self.num)
		print(sql)
		try:
			self.cur_out.execute(sql)
			results = self.cur_out.fetchall()
			return results
		except:
			traceback.print_exc()
		return None

	def insertManyFun(self, args_list):
		"""
		多条插入函数
		:param args_list:
		:return:
		"""
		sql = """insert into {db}.{tab} {col} VALUES ({val})""".format(db=self.db_in, tab=self.tab_in,
		                                                                 col=self.col_in, val=self.val_str)
		print(sql)
		try:
			self.cur_in.executemany(sql, args_list)
			self.conn_in.commit()
		except:
			traceback.print_exc()


def main(start, config):
	"""
	主函数，逻辑为循环查询，去掉除name之外所有为空的行，并50000条插入
	:param start:
	:param config:
	:return:
	"""
	extract = Extract(tab_out=config['sel_table'], tab_in=config['inser_table'], col_out=config['sel_columns'],
	                  col_in=config['inser_columns'], db_out=config['db'], )
	while True:
		results = extract.selectFun(start)
		if not results:
			# import time
			# time.sleep(400)
			# continue
			print('no datas...')
			exit(1)
		value_list = []
		for result in results:
			start += 1
			print(start)
			# 去空，当空字段的个数大于要查询的字段个数时，说明除了comp_full_name之外所有字段都是空的
			n = 0
			for val in result.values():
				if val == '' or val is None:
					n += 1
			if n >= extract.col_out_num - 1:
				continue
			values = [result[extract.col_out_list[i].strip()] for i in range(extract.col_out_num)]
			value_list.append(values)
			if len(value_list) == 50000:
				extract.insertManyFun(value_list)
				value_list.clear()
			else:
				continue
		extract.insertManyFun(value_list)


if __name__ == '__main__':
	"""传入三个参数
	第一个为插入表格 tyc_jichu_quan
	第二个是插入类型 base intro logo officeaddr registaddr shortname teaminfo web
	第三个是查询游标 15384877
	"""
	tab_out = sys.argv[1]
	in_cat = sys.argv[2]
	start = int(sys.argv[3])
	for conf in config_list:
		if tab_out == conf['sel_table'] and in_cat in conf['inser_table']:
			main(start, conf)
			break
		else:
			print('Dont find this out table or insert categary is wrong,please insert again!')
			exit(1)
