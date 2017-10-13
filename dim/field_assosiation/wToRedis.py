import redis
import pymysql

QUEUE_REDIS_HOST = 'a027.hb2.innotree.org'
QUEUE_REDIS_PORT = 6379

pool = redis.ConnectionPool(host=QUEUE_REDIS_HOST, port=QUEUE_REDIS_PORT)
db = redis.StrictRedis(connection_pool=pool, decode_responses=True)


def _sqlObj():
	connect = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider',
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	return connect


def _sqlObj_new():
	connect = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider',
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	return connect


def in_redis(db, tab):
	mysql = _sqlObj()
	mysql.select_db(db)
	cur = mysql.cursor()
	sql = """select comp_full_name, t_id from {tab}""".format(tab=tab)
	cur.execute(sql)
	results = cur.fetchall()
	for i, r in enumerate(results):
		comp_full_name = r['comp_full_name']
		t_id = r['t_id']
		db.hmset('tyc_jichu_quan', {t_id: comp_full_name})
		print(i)


if __name__ == '__main__':
	pass
