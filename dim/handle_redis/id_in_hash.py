"""
255之外补录的数据（只有id）
步骤：
1、dw_dim_online.linshi_com 取出 c_name
2、dimension_sum.com_dictionaries 用 only_id 搜索 name
3、放入redis 2622_only_id 中
"""
import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
# import redis
import traceback
from dim.utility.tools import get_redis_db, in_redis_hash


# def isRegister(_oneid):
# 	"""
# 	判断一个 ID 是否注册
# 	:param _oneid:
# 	:return:
# 	"""
# 	r = redis.Redis(host='10.44.51.90', port=6379, db=0)
# 	return r.sismember(name="zhuce", value=_oneid)
#
#
# def insert_redis():
# 	"""
# 	入 id：name
# 	:return:
# 	"""
# 	sql_config = {'host': '47.95.31.183',
# 	              'port': 3306,
# 	              'user': 'test',
# 	              'password': '123456',
# 	              # 'db': 'innotree_data_online',
# 	              'charset': 'utf8',
# 	              'cursorclass': pymysql.cursors.DictCursor}
# 	mysql1 = get_mysql_con(config=sql_config)
# 	mysql1.select_db(db='innotree_data_online')
# 	cur1 = mysql1.cursor()
#
# 	aa_config = {'host': 'etl1.innotree.org',
# 	             'port': 3308,
# 	             'user': 'spider',
# 	             'password': 'spider',
# 	             # 'db': 'dimension_result',
# 	             'charset': 'utf8',
# 	             'cursorclass': pymysql.cursors.DictCursor}
# 	mysql2 = get_mysql_con(config=aa_config)
# 	mysql2.select_db(db='dimension_sum')
# 	cur2 = mysql2.cursor()
# 	try:
# 		sql1 = """select c_name from linshi_com"""
# 		cur1.execute(sql1)
# 		results1 = cur1.fetchall()
# 		print(results1[0])
# 		result1_list = [res['c_name'] for res in results1]
# 		n = []
# 		start = 0
# 		for m in result1_list:
# 			n.append(m)
# 			if len(n) == 10000:
# 				sql2 = """select be_company_name, only_id from com_dictionaries WHERE `only_id` in {x}""".format(
# 					x=str(tuple(n)))
# 				cur2.execute(sql2)
# 				results2 = cur2.fetchall()
#
# 				redis_db = get_redis_db(host='a027.hb2.innotree.org')
# 				for result in results2:
# 					start += 1
# 					print(start)
# 					if isRegister(result['only_id']):
# 						in_redis_hash(redis_db, '2622_only_id', result['only_id'], result['be_company_name'])
# 				n.clear()
# 			else:
# 				continue
#
# 		sql2 = """select be_company_name, only_id from com_dictionaries WHERE `only_id` in {x}""".format(
# 			x=str(tuple(n)))
# 		cur2.execute(sql2)
# 		results2 = cur2.fetchall()
#
# 		redis_db = get_redis_db(host='a027.hb2.innotree.org')
# 		for result in results2:
# 			start += 1
# 			print(start)
# 			if isRegister(result['only_id']):
# 				in_redis_hash(redis_db, '2622_only_id', result['only_id'], result['be_company_name'])
#
# 	except:
# 		traceback.print_exc()
# 	finally:
# 		mysql1.close()
# 		mysql2.close()


def in_redis_id(conf, tab, col, re_key):
	"""
	只入id
	:param conf:
	:param col:
	:param tab:
	:param re_key:
	:return:
	"""
	mysql = pymysql.connect(**conf)
	cur = mysql.cursor()
	try:
		sql = """select {col} from {tab}""".format(col=col, tab=tab)
		cur.execute(sql)
		results = cur.fetchall()

		redis_db = get_redis_db(host='a027.hb2.innotree.org')
		for i, result in enumerate(results):
			print(i)
			in_redis_hash(redis_db, re_key, result[col], '')

	except:
		traceback.print_exc()
	finally:
		mysql.close()


if __name__ == '__main__':
	online_config = {'host': '47.95.31.183',
	                 'port': 3306,
	                 'user': 'test',
	                 'password': '123456',
	                 'db': 'innotree_data_online',
	                 'charset': 'utf8',
	                 'cursorclass': pymysql.cursors.DictCursor}
	in_redis_id(online_config, 'comp_gaoxin', 'comp_id', 'comp_gaoxin_only_id')
