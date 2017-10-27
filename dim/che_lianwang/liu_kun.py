"""
从result中取出 city=柳州、昆明的 only_id 、company_full_name 、city放到一个表中，宏宇再放进去
"""
import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])
import pymysql
from dim.utility.tools import get_redis_db, get_redis_field, _handle_str, hexists
from dim.utility.info import a027, etl_config, online_config

a027_db = get_redis_db(a027)

etl = pymysql.connect(**etl_config)
etl.select_db('dimension_result')
result_cur = etl.cursor()

etl.select_db('spider')
spider_cur = etl.cursor()

sql = """select only_id, comp_full_name, city from comp_registaddr_result0 WHERE city = '柳州市'"""


