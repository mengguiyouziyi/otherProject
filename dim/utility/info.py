import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
from dim.utility.tools import get_redis_db

a027_db = get_redis_db(host='a027.hb2.innotree.org')
a024_db = get_redis_db(host='10.44.152.49', db=10)


etl_config = {'host': 'etl1.innotree.org',
              'port': 3308,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}

online_config = {'host': '47.95.31.183',
                 'port': 3306,
                 'user': 'test',
                 'password': '123456',
                 'db': 'innotree_data_online',
                 'charset': 'utf8',
                 'cursorclass': pymysql.cursors.DictCursor}

xin_config = {'host': '10.252.0.52',
              'port': 3306,
              'user': 'etl_tmp',
              'password': 'UsF4z5HE771KQpra',
              'db': 'tianyancha',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
