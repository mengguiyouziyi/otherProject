"""
jsp文件中老的id换成新的id
说明：
1、读取文件，获取旧的 id 和 short
2、用 id - comp_id 查找 innotree_data.company_base_info 中的 comp_full_name
3、用 comp_full_name 查找 innotree_data_online.company_base_info 中的 comp_id、comp_short_name
4、插入到新表 innotree_data.old_to_new
"""

import re
import pymysql
import os

config = {'host': '47.95.31.183',
             'port': 3306,
             'user': 'test',
             'password': '123456',
             'db': 'innotree_data',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}
mysql = pymysql.connect(**config)
cursor = mysql.cursor()

new_config = {'host': '47.95.31.183',
             'port': 3306,
             'user': 'test',
             'password': '123456',
             'db': 'innotree_data_online',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}
new_mysql = pymysql.connect(**new_config)
new_cursor = new_mysql.cursor()

dir_path = "/Users/menggui/Desktop/newchain/"
paths = [os.path.join(dir_path, f) for f in os.listdir(dir_path)]

id_short_list = []
for path in paths:
	with open(path, 'r') as f:
		x = f.read()
		co = re.compile(r'\<a href="/inno/company/(\d+?)\.html" target="view_window" class="in_se_a03"\>(.+?)\</a\>')
		se = re.findall(co, x)
		id_short_list.extend(se)
# sql_0 = """insert into innotree_data.old_to_new (old_comp_id, old_comp_short_name) VALUES (%s, %s)"""
# cursor.executemany(sql_0, id_short_list)
# mysql.commit()
# mysql.close()



# 在老表中查找其中的全称
id_list = [f[0] for f in id_short_list]
print(id_list)
sql_1 = """select comp_id, comp_full_name, comp_source from company_base_info WHERE comp_id in {}""".format(str(tuple(id_list)))
cursor.execute(sql_1)
r1 = cursor.fetchall()
print(r1)

# id_1_list = [r['comp_id'] for r in r1 if r['comp_source'] != 4]
# up_sql_1 = """update old_to_new set comp_full_name = %s WHERE old_comp_id = %s"""
# print(up_sql_1)
# values_1_list = [(r['comp_full_name'], r['comp_id']) for r in r1 if r['comp_source'] != 4]
# print(values_1_list)
# cursor.executemany(up_sql_1, values_1_list)
# mysql.commit()


# 用全称查找comp_id和short_name
sql_2 = """select comp_id, comp_full_name, comp_short_name from innotree_data_online.company_base_info WHERE comp_full_name in {}""".format(str(tuple([r['comp_full_name'] for r in r1])))
new_cursor.execute(sql_2)
r2 = new_cursor.fetchall()

up_sql_2 = """update old_to_new set new_comp_id = %s, new_comp_short_name = %s WHERE comp_full_name = %s"""
values_2_list = [(r['comp_id'], r['comp_short_name'], r['comp_full_name']) for r in r2]
cursor.executemany(up_sql_2, values_2_list)
mysql.commit()

# sql_3 = """insert into innotree_data.old_to_new (old_comp_id, old_comp_short_name, comp_full_name, new_comp_id, new_comp_short_name) VALUES (%s, %s, %s, %s, %s)"""
# values_list = []
# cursor.execute(sql_3, values_list)
# mysql.commit()
















