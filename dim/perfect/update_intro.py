"""
暂时没用
"""
import pymysql
from outAndIn import get_redis_db, get_mysql_con, get_redis_field, _handle_str

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
             'db': 'innotree_data_online',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}

# 创建查询sql连接和游标
sel_con = get_mysql_con(config=sel_config)
sel_cur = sel_con.cursor()
# 创建插入sql连接和游标
in_con = get_mysql_con(config=in_config)
in_cur = in_con.cursor()

sql = """select comp_id from company_base_info WHERE comp_introduction is not null"""
up_sql = """update company_base_info set comp_introduction = % WHERE """