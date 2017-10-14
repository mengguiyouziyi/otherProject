"""
将某个纬度的十张表，id和full_name全部入到redis中
"""
import pymysql
from outAndIn import get_mysql_con, get_redis_db, in_redis_hash

sel_config = {'host': 'etl1.innotree.org',
              'port': 3308,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
up_con = get_mysql_con(config=sel_config)
up_cur = up_con.cursor()

results = []
for i in range(10):
	sql = """select * from comp_intro_result{}""".format(i)
	up_cur.execute(sql)
	rs = up_cur.fetchall()
	results.extend(rs)
redis_db = get_redis_db(host='a027.hb2.innotree.org')
start = 0
for result in results:
	start += 1
	print(start)
	in_redis_hash(redis_db, 'intro_all_only_id', result['only_id'], result['comp_full_name'])
