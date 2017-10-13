"""
查找255万中存在，但是没有入到company_base_info中的公司
"""

import pymysql
from outAndIn import get_mysql_con, get_redis_db, get_redis_allhash

# sel_config = {'host': 'etl1.innotree.org',
#               'port': 3308,
#               'user': 'spider',
#               'password': 'spider',
#               'db': 'dimension_result',
#               'charset': 'utf8',
#               'cursorclass': pymysql.cursors.DictCursor}
sel_config = {'host': '47.95.31.183',
              'port': 3306,
              'user': 'test',
              'password': '123456',
              'db': 'innotree_data',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}

# 创建插入sql连接和游标
con = get_mysql_con(config=sel_config)
cur = con.cursor()
results = []
sta = 0
while True:
	sql = """select comp_id, comp_full_name from company_base_info limit {sta}, 200000""".format(sta=sta)
	cur.execute(sql)
	res = cur.fetchall()
	if not res:
		break
	sta += len(res)
	print(res[0])
	results.extend(res)
print(results[0])
result_dict = {result['comp_id']: result['comp_full_name'] for result in results}

# 创建redis连接并获取所有only_id
redis_db = get_redis_db(host='a027.hb2.innotree.org')
id_names = get_redis_allhash(redis_db, '200w_only_id')
id_name = {k.decode('utf-8'): v.decode('utf-8') for k, v in id_names.items()}
print(type(id_name))

cha_list = list(set(id_name.keys())^set(result_dict.keys()))
print(cha_list[:3])
# chas = [{'comp_id': cha, 'comp_full_name': id_name[cha]} for cha in cha_list]
# cha_dict = {cha: id_name[cha] for cha in cha_list}

# redis_dict = {'comp_id': id_name, 'comp_full_name': id_name}

in_sql = """insert into company_base_info_nohave (comp_id, comp_full_name) VALUES (%s, %s)"""
value_list = [[cha, id_name[cha]] for cha in cha_list]
print(value_list[0])
cur.executemany(in_sql, args=value_list)
con.commit()
