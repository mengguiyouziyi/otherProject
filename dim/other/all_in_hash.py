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
from dim.utility.tools import get_redis_db, in_redis_hash

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
			comp_id = result['comp_id']
			comp_full_name = result['comp_full_name']
			in_redis_hash(redis_db, 'id_name_all', comp_id, comp_full_name)
			in_redis_hash(redis_db, 'name_id_all', comp_full_name, comp_id)
		sta += len(results)
		print(sta)
	all_ids += sta
	print('~~~~~~~~' + str(n) + '~~~~~~~~' + str(all_ids) + '~~~~~~~~')
