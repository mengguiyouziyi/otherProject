"""
255之外补录的数据
步骤：
1、dw_dim_online.company_bulu_it取出公司
2、dimension_sum.com_dictionaries 查询only_id
3、放入redis 8800_only_id 中
"""
import pymysql
import redis
import traceback
from tools import get_redis_db, in_redis_hash, get_mysql_con


def isRegister(_oneid):
	"""
	判断一个 ID 是否注册
	:param _oneid:
	:return:
	"""
	r = redis.Redis(host='10.44.51.90', port=6379, db=0)
	return r.sismember(name="zhuce", value=_oneid)


def insert_redis():
	sql_config = {'host': 'etl1.innotree.org',
	              'port': 3308,
	              'user': 'spider',
	              'password': 'spider',
	              # 'db': 'dimension_result',
	              'charset': 'utf8',
	              'cursorclass': pymysql.cursors.DictCursor}
	mysql1 = get_mysql_con(config=sql_config)
	mysql1.select_db(db='dw_dim_online')
	cur1 = mysql1.cursor()

	mysql2 = get_mysql_con(config=sql_config)
	mysql2.select_db(db='dimension_sum')
	cur2 = mysql2.cursor()
	try:
		sql1 = """select company_full_name, data_from from company_bulu_it"""
		cur1.execute(sql1)
		results1 = cur1.fetchall()
		print(results1[0])
		result1_list = [res['company_full_name'] for res in results1 if not res['data_from']]
		n = []
		start = 0
		for m in result1_list:
			n.append(m)
			if len(n) == 10000:
				sql2 = """select be_company_name, only_id from com_dictionaries WHERE `be_company_name` in {x}""".format(
					x=str(tuple(n)))
				cur2.execute(sql2)
				results2 = cur2.fetchall()

				redis_db = get_redis_db(host='a027.hb2.innotree.org')
				for result in results2:
					start += 1
					print(start)
					if isRegister(result['only_id']):
						in_redis_hash(redis_db, '10w_only_id', result['only_id'], result['be_company_name'])

				n.clear()
			else:
				continue

		sql2 = """select be_company_name, only_id from com_dictionaries WHERE `be_company_name` in {x}""".format(
			x=str(tuple(n)))
		cur2.execute(sql2)
		results2 = cur2.fetchall()

		redis_db = get_redis_db(host='a027.hb2.innotree.org')
		for result in results2:
			start += 1
			print(start)
			if isRegister(result['only_id']):
				in_redis_hash(redis_db, '10w_only_id', result['only_id'], result['be_company_name'])

	except:
		traceback.print_exc()
	finally:
		mysql1.close()
		mysql2.close()


if __name__ == '__main__':
	insert_redis()
