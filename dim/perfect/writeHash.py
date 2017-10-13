import pymysql
from outAndIn import get_redis_db, in_redis_hash, get_mysql_con, sel_fun

sql_config = {'host': '47.95.31.183',
              'port': 3306,
              'user': 'test',
              'password': '123456',
              'db': 'innotree_data',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
mysql = get_mysql_con(config=sql_config)
cur = mysql.cursor()
redis_db = get_redis_db(host='a027.hb2.innotree.org')
start = 0
# while True:
# results = sel_fun(mysql, 'innotree_data', 'company_base_info_nohave', 'comp_full_name,comp_id', start)
sql = """select comp_full_name,comp_id from company_base_info_nohave"""
cur.execute(sql)
results = cur.fetchall()
# print(results[0:10])
# if not results:
# 	break
for result in results:
	# print(result)
	start += 1
	print(start)
	# if result['zhuce_or'] == 0:
	in_redis_hash(redis_db, '9w_only_id', result['comp_id'], result['comp_full_name'])
