# coding:utf-8
import pymysql
import traceback
import os
import sys
import logging
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def selectFun(columns, tab, start, num, db='spider'):
	"""
	查询并返回结果
	参数：字段，表
	:return:
	"""
	select_sql = """select {columns} from {tab} limit {start}, {num}""".format(
		columns=columns, tab=tab, start=start, num=num)
	print(select_sql)
	select_con, select_cur = _sqlObj(db)
	try:
		select_cur.execute(select_sql)
		results = select_cur.fetchall()
		return results
	except:
		traceback.print_exc()
	finally:
		select_con.close()
	return None


# def insertFun(insert_con, insert_cur, tab, columns, args):
# 	"""
# 	结果插入表
# 	参数：表， 字段， 字段值
# 	"""
# 	insert_sql = """insert into {tab} {columns} VALUES (%s, %s)""".format(tab=tab, columns=columns)
#
# 	insert_cur.execute(insert_sql, args)
# 	insert_con.commit()


def insertManyFun(tab, columns, args_list):
	"""
	结果插入表，批量，不利于
	参数：表， 字段， 字段值
	"""
	col_num = len(columns.split(', '))
	insert_sql = """insert into {tab} {columns} VALUES {val}""".format(tab=tab, columns=columns,
	                                                                   val=_handle_str(col_num))
	print(insert_sql)
	insert_con, insert_cur = _sqlObj('spider_dim')
	try:
		insert_cur.executemany(insert_sql, args_list)
		insert_con.commit()
	except:
		traceback.print_exc()
	finally:
		insert_con.close()


def _handle_str(num):
	"""
	根据插入字段数量来构造sql语句
	:param num: 插入字段数量
	:return: sql的value字符串
	"""
	x = "(%s"
	y = ", %s"
	for i in range(num - 1):
		x += y
	return x + ')'


def _sqlObj(db):
	"""
	etl1.innotree.org
	参数：数据库
	"""
	connect = pymysql.connect(host='172.31.215.38', port=3306, user='spider', password='spider', db=db,
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = connect.cursor()
	return connect, cursor


def _sqlObj1(db):
	"""
	10.252.0.52
	参数：数据库
	"""
	connect = pymysql.connect(host='10.252.0.52', port=3306, user='etl_tmp', password='UsF4z5HE771KQpra', db=db,
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = connect.cursor()
	return connect, cursor


def main(*args):
	columns_list = args[0].split(',')
	num = len(columns_list)
	# shunqi 12582242
	start = i = 0
	while True:
		results = selectFun(args[0], args[1], start, 500000, db=args[2])
		if not results:
			time.sleep(400)
			continue
			# return
		start += len(results)
		value_list = []
		for result in results:
			i += 1
			print(i)
			# 去空
			n = 0
			for val in result.values():
				if val == '' or val is None:
					n += 1
			if n >= num - 1:
				continue
			values = [result[columns_list[i].strip()] for i in range(num)]
			value_list.append(values)
			if len(value_list) == 50000:
				insertManyFun(args[3], args[4], value_list)
				value_list.clear()
			else:
				continue
		insertManyFun(args[3], args[4], value_list)


if __name__ == '__main__':
	# select_columns = "quan_cheng, logo"
	# select_table = "tyc_jichu_chuisou"
	#
	# insert_table = "comp_logo_tyc"
	# insert_columns = "(comp_full_name, logo_url)"
	# args = [select_columns, select_table, insert_table, insert_columns]
	# main(*args)
	pass
