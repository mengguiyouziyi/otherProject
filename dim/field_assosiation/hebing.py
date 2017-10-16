import pymysql
import os
import logging
import redis
import time

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)


QUEUE_REDIS_HOST = '10.44.152.49'
QUEUE_REDIS_PORT = 6379

pool = redis.ConnectionPool(host=QUEUE_REDIS_HOST, port=QUEUE_REDIS_PORT, db=10)
db = redis.StrictRedis(connection_pool=pool, decode_responses=True)


def _sqlObj(db):
	"""
	连接数据库并获取游标
	参数：数据库
	"""
	connect = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db=db,
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	return connect


def _sqlObj1(db):
	"""
	连接数据库并获取游标
	参数：数据库
	"""
	connect = pymysql.connect(host='10.252.0.52', port=3306, user='etl_tmp', password='UsF4z5HE771KQpra', db=db,
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	return connect


def selectFun(con, tab, start):
	sql = """select * from {tab} limit {start}, 500000""".format(tab=tab, start=start)
	# print(sql)
	cur = con.cursor()
	cur.execute(sql)
	return cur.fetchall()


def insertManyFun(insert_con, tab, args_list):
	"""
	结果插入表，批量，不利于
	参数：表， 字段， 字段值
	"""
	columns_a = _get_column(insert_con, tab)
	col_num = len(columns_a.split(','))
	columns = '(' + columns_a + ')'
	insert_sql = """insert into {tab} {columns} VALUES {val}""".format(tab=tab, columns=columns,
	                                                                   val=_handle_str(col_num))
	# print(insert_sql)
	# print(args_list[0])
	insert_cur = insert_con.cursor()

	insert_cur.executemany(insert_sql, args_list)
	insert_con.commit()


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


def _get_redis(t_id):
	return db.get(t_id)
	# return db.hget('jigou_base_smt', s_id)


def _get_column(con, table_in):
	sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{a}' and table_schema = '{b}'""".format(
		a=table_in, b='spider_dim')
	cur = con.cursor()
	cur.execute(sql)
	results = cur.fetchall()
	columns = results[0]['group_concat(column_name)'][3:-10]
	return columns


def main(table_get, table_in):
	# 用于搜索的mysql连接
	sel_con = _sqlObj1('tianyancha')
	# 用于插入的mysql连接
	in_con = _sqlObj('spider_dim')
	# in_col = _get_column(in_con, table_in)

	start = i = 9693
	while True:
		results = selectFun(sel_con, table_get, start=start)
		if not results:
			# time.sleep(300)
			# continue
			break
		start += len(results)
		value_list = []
		for result in results:
			i += 1
			print(i)
			comp_full_name = _get_redis(result['t_id'])
			result['comp_full_name'] = comp_full_name if comp_full_name else ''
			# columns_list = in_col.split(',')
			# values = [result[column] for column in columns_list]
			values = [result['comp_full_name'], result['t_id'], result['m_name'], result['m_position'], '', '', result['logo_url'], '', '', result['m_experience']]
			value_list.append(values)
			if len(value_list) == 50000:
				insertManyFun(in_con, table_in, value_list)
				print('done')
				value_list.clear()
			else:
				continue
		insertManyFun(in_con, table_in, value_list)


if __name__ == '__main__':
	pass
