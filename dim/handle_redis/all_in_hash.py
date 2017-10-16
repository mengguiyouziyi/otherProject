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
from dim.utility.tools import get_redis_db, in_redis_hash

# redis_db = get_redis_db(host='a027.hb2.innotree.org')
redis_db = get_redis_db(host='a027.hb2.innotree.org')
sel_config = {'host': 'etl1.innotree.org',
              'port': 3308,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
sel_mysql = pymysql.connect(**sel_config)
sel_cur = sel_mysql.cursor()


def in_redis_all_tycid():
	"""
	将全量天眼查id入到redis总量key中
	:return:
	"""
	sta = 4000000
	while True:
		all_sql = """select t_id, quan_cheng from tyc_jichu_quan limit {sta}, 500000""".format(nsta=sta)
		sel_cur.execute(all_sql)
		results = sel_cur.fetchall()
		if not results:
			break
		for result in results:
			comp_id = result['t_id']
			comp_full_name = result['quan_cheng']
			in_redis_hash(redis_db, 'tycid_name_all', comp_id, comp_full_name)
		sta += len(results)
		print(sta)


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
			sel_cur.execute(all_sql)
			results = sel_cur.fetchall()
			if not results:
				break
			for result in results:
				comp_id = result['only_id']
				comp_full_name = result['comp_full_name']
				in_redis_hash(redis_db, 'id_name_all', comp_id, comp_full_name)
				in_redis_hash(redis_db, 'name_id_all', comp_full_name, comp_id)
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
			sel_cur.execute(all_sql)
			results = sel_cur.fetchall()
			if not results:
				break
			for result in results:
				comp_id = result['only_id']
				in_redis_hash(redis_db, re_key, comp_id, '')
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
		sel_mysql.close()
