"""
按照尾号 only_id:comp_full_name 放入 id_name_all
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

etl = pymysql.connect(**etl_config)
etl.select_db('dimension_result')
etl_cur = etl.cursor()


def in_redis_num():
	"""
	按尾号将id插入redis不同key中（全量）
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
		in_redis_num()
	except:
		traceback.print_exc()
	finally:
		etl.close()
