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
from rediscluster import StrictRedisCluster
# from dim.utility.tools import in_redis_hash
# from dim.utility.info import a024, a027, etl_config, xin_config, online_config

startup_nodes = [{"host": "172.29.237.209", "port": "7000"},
                 {"host": "172.29.237.209", "port": "7001"},
                 {"host": "172.29.237.209", "port": "7002"},
                 {"host": "172.29.237.214", "port": "7003"},
                 {"host": "172.29.237.214", "port": "7004"},
                 {"host": "172.29.237.214", "port": "7005"},
                 {"host": "172.29.237.215", "port": "7006"},
                 {"host": "172.29.237.215", "port": "7007"},
                 {"host": "172.29.237.215", "port": "7008"}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
etl_config = {'host': '172.31.215.38',
              'port': 3306,
              'user': 'spider',
              'password': 'spider',
              # 'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
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
				# comp_id = result['only_id']
				comp_full_name = result['comp_full_name']
				rc.sadd('zhuce_names', comp_full_name)
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
