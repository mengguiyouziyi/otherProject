"""
将 only_id:comp_full_name 放入 id_name_all
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


def in_redis_all():
	"""
	将全量id入到redis总量key中（全量）
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


if __name__ == '__main__':
	try:
		in_redis_all()
	except:
		traceback.print_exc()
	finally:
		etl.close()
