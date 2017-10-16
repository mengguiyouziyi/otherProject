"""
将需要增补为线上数据的公司，放入redis中
"""
import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
import traceback
from dim.utility.tools import get_redis_db, in_redis_hash, in_redis_string
from dim.utility.info import a024, a027, etl_config, xin_config, online_config

a027_db = get_redis_db(a027)
# a024_db = get_redis_db(a024)

etl = pymysql.connect(**etl_config)
etl.select_db('tyc')
etl_cur = etl.cursor()


# xin = pymysql.connect(**xin_config)
# xin.select_db('tianyancha')
# xin_cur = xin.cursor()
#
# online = pymysql.connect(**online_config)
# online.select_db('innotree_data_online')
# online_cur = online.cursor()


def in_redis_all():
	"""
	将全量id入到redis总量key中
	:return:
	"""
	all_ids = 0
	for n in range(10):
		sta = 0
		while True:
			all_sql = """select only_id, comp_full_name from comp_base_result{num} limit {sta}, 500000""".format(num=n,
			                                                                                                     sta=sta)
			etl_cur.execute(all_sql)
			results = etl_cur.fetchall()
			if not results:
				break
			for result in results:
				comp_id = result['only_id']
				comp_full_name = result['comp_full_name']
				in_redis_hash(a027_db, 'id_name_all', comp_id, comp_full_name)
				in_redis_hash(a027_db, 'name_id_all', comp_full_name, comp_id)
			sta += len(results)
			print(sta)
		all_ids += sta
		print('~~~~~~~~' + str(n) + '~~~~~~~~' + str(all_ids) + '~~~~~~~~')


def in_redis_num():
	"""
	按尾号将id插入redis不同key中
	:return:
	"""
	all_ids = 0
	for n in range(10):
		re_key = 'id_name_all_{num}'.format(num=n)
		sta = 0
		while True:
			all_sql = """select only_id from comp_base_result{num} limit {sta}, 500000""".format(num=n, sta=sta)
			etl_cur.execute(all_sql)
			results = etl_cur.fetchall()
			if not results:
				break
			for result in results:
				comp_id = result['only_id']
				in_redis_hash(a027_db, re_key, comp_id, '')
			sta += len(results)
			print(sta)
		all_ids += sta
		print('~~~~~~~~' + str(n) + '~~~~~~~~' + str(all_ids) + '~~~~~~~~')


if __name__ == '__main__':
	try:
		# in_redis_all()
		in_redis_num()
	except:
		traceback.print_exc()
	finally:
		etl.close()
