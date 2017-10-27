"""
宏宇要如redis，set
"""
import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
from dim.utility.tools import get_redis_db
from dim.utility.info import a024, a027, etl_config, xin_config, online_config

a024_db = get_redis_db(a024)

etl = pymysql.connect(**etl_config)
etl.select_db('spider')
etl_cur = etl.cursor()

sql = """select cname from zhuanli_redis"""
etl_cur.execute(sql)
results = etl_cur.fetchall()

for i, result in enumerate(results):
	print(i)
	if not result['cname']:
		continue
	a024_db.sadd('buchong', result['cname'])
