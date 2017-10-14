"""
查找255万中存在，但是没有入到company_base_info中的公司
"""

import pymysql
from outAndIn import get_mysql_con, get_redis_db, get_redis_allhash, in_redis_hash

sel_config = {'host': '47.95.31.183',
              'port': 3306,
              'user': 'test',
              'password': '123456',
              'db': 'innotree_data_online',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}

# 创建插入sql连接和游标
con = get_mysql_con(config=sel_config)
cur = con.cursor()

# 全量读取 company_base_info 中 comp_id, comp_full_name
results = []
sta = 0
while True:
	sql = """select comp_id, comp_full_name from company_base_info limit {sta}, 200000""".format(sta=sta)
	cur.execute(sql)
	res = cur.fetchall()
	if not res:
		break
	sta += len(res)
	# print(res[0])
	results.extend(res)
# print(results[0])
result_dict = {result['comp_id']: result['comp_full_name'] for result in results}  # 做成id：name的全集字典

# 全量取出redis中的 comp_id, comp_full_name
redis_db = get_redis_db(host='a027.hb2.innotree.org')
id_names = get_redis_allhash(redis_db, 'intro_all_only_id')
id_name = {k.decode('utf-8'): v.decode('utf-8') for k, v in id_names.items()}
# print(type(id_name))

# 取两个的差集（redis - company_base_info）
id_cha_list = list(set(id_name.keys()) - set(result_dict.keys()))
# print(id_cha_list[:3])
# chas = [{'comp_id': cha, 'comp_full_name': id_name[cha]} for cha in cha_list]
# cha_dict = {cha: id_name[cha] for cha in cha_list}

# redis_dict = {'comp_id': id_name, 'comp_full_name': id_name}

# # 将这部分差集放入 company_base_info_nohave
# in_sql = """insert into company_base_info_nohave (comp_id, comp_full_name) VALUES (%s, %s)"""
# value_list = [[id, id_name[id]] for id in id_cha_list]
# # print(value_list[0])
# m = []
# for i, n in enumerate(value_list):
# 	m.append(n)
# 	print(i)
# 	if len(m) == 50000:
# 		cur.executemany(in_sql, args=value_list)
# 		con.commit()
# 		m.clear()
# 	else:
# 		continue
# cur.executemany(in_sql, args=value_list)
# con.commit()
# con.close()

# 将这部分数据放入 redis
value_list = [[id, id_name[id]] for id in id_cha_list]
print(value_list[0])
start = 0
for result in value_list:
	start += 1
	print(start)
	in_redis_hash(redis_db, 'intro_no_only_id', result[0], result[1])








