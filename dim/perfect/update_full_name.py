import pymysql
import traceback
from outAndIn import get_mysql_con

sel_config = {'host': 'etl1.innotree.org',
              'port': 3308,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}

in_config = {'host': '47.95.31.183',
             'port': 3306,
             'user': 'test',
             'password': '123456',
             'db': 'innotree_data',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}
# 创建查询sql连接和游标
sel_con = get_mysql_con(config=sel_config)
sel_cur = sel_con.cursor()
# 创建插入sql连接和游标
in_con = get_mysql_con(config=in_config)
in_cur = in_con.cursor()
results_list = []
try:
	for i in range(10):
		sel_sql = """select comp_full_name, only_id from comp_base_result{}""".format(i)
		print(sel_sql)
		sel_cur.execute(sel_sql)
		results = sel_cur.fetchall()
		print(results[0])
		results_list.extend(results)
	print(len(results_list))
	up_sql = """update company_base_info set comp_full_name = %s WHERE `comp_id` = %s"""
	value_list = [(result['comp_full_name'], result['only_id']) for result in results_list]
	in_cur.executemany(up_sql, value_list)
	in_con.commit()
except:
	traceback.print_exc()
finally:
	in_con.close()
