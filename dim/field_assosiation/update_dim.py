import pymysql
import redis
import time

connect = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider_dim',
                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()

QUEUE_REDIS_HOST = '10.44.152.49'
QUEUE_REDIS_PORT = 6379

pool = redis.ConnectionPool(host=QUEUE_REDIS_HOST, port=QUEUE_REDIS_PORT, db=10)
redis_db = redis.StrictRedis(connection_pool=pool, decode_responses=True)


def sel_fun(tab, sta):
	sql = """select t_id from {tab} where comp_full_name is null limit {sta},{lim}""".format(tab=tab, sta=sta,
	                                                                                         lim=500000)
	print(sql)
	cursor.execute(sql)
	connect.commit()
	results = cursor.fetchall()
	return results


def update_dim(tab, value_list):
	sql = """update {tab} set comp_full_name = %s WHERE t_id = %s""".format(tab=tab)
	print(sql)
	cursor.executemany(sql, value_list)
	connect.commit()


def main(tab):
	sta = 0
	while True:
		results = sel_fun(tab, sta)
		if not results:
			# time.sleep(60)
			# continue
			return
		sta += len(results)
		value_list = []
		for i, result in enumerate(results):
			t_id = result['t_id']
			name = redis_db.get(t_id)
			values = [name, t_id]
			value_list.append(values)
			print(i + 1)
			if len(value_list) > 20000:
				update_dim(tab, value_list)
				value_list.clear()
			else:
				continue
		update_dim(tab, value_list)


if __name__ == '__main__':
	# for tab in ['comp_duiwai_tyc', 'comp_gudong_tyc']:
	# 	main(tab)
	main('comp_duiwai_tyc')
