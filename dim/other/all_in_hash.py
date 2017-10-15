"""
将需要增补为线上数据的公司，放入redis中
"""

import pymysql
import redis
from tools import get_redis_db, in_redis_hash, get_mysql_con


def isRegister(_oneid):
	"""
	判断一个 ID 是否注册
	:param _oneid:
	:return:
	"""
	r = redis.Redis(host='10.44.51.90', port=6379, db=0)
	return r.sismember(name="zhuce", value=_oneid)


sel_config = {'host': 'etl1.innotree.org',
              'port': 3308,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
sel_mysql = pymysql.connect(**sel_config)
sel_cur = sel_mysql.cursor()
sta = 0
for n in range(10):
	while True:
		all_sql = """select only_id, comp_full_name from comp_base_result{num} limit {sta}, 500000""".format(num=n,
		                                                                                                     sta=sta)
		sel_cur.execute(all_sql)
		rs = sel_cur.fetchall()
		if not rs:
			break






sql_config = {'host': '47.95.31.183',
              'port': 3306,
              'user': 'test',
              'password': '123456',
              'db': 'innotree_data_online',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}

mysql = get_mysql_con(config=sql_config)
cur = mysql.cursor()

results = []
sta = 0
while True:
	sql = """select comp_id, comp_full_name from input_comp_tag limit {sta}, 400000""".format(sta=sta)
	cur.execute(sql)
	res = cur.fetchall()
	if not res:
		break
	sta += len(res)
	results.extend(res)

redis_db = get_redis_db(host='a027.hb2.innotree.org')
start = 0
for result in results:
	start += 1
	print(start)
	if isRegister(result['comp_id']):
		in_redis_hash(redis_db, 'tag_only_id', result['comp_id'], result['comp_full_name'])
