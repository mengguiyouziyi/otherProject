"""
将需要增补为线上数据的公司，放入redis中
"""
import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
import traceback
from dim.utility.tools import get_redis_db, in_redis_hash, in_redis_string
from dim.utility.info import a024, a027, etl_config, xin_config, online_config

a027_db = get_redis_db(a027)
# a024_db = get_redis_db(a024)

setl = pymysql.connect(**etl_config)
setl.select_db('spider')
setl_cur = setl.cursor()

etl = pymysql.connect(**etl_config)
etl.select_db('tyc')
etl_cur = etl.cursor()

xin = pymysql.connect(**xin_config)
xin.select_db('tianyancha')
xin_cur = xin.cursor()
#
# online = pymysql.connect(**online_config)
# online.select_db('innotree_data_online')
# online_cur = online.cursor()


def in_redis_all_tycid(cur, tab, sta=0):
	"""
	将全量t_id入到redis总量key中
	:return:
	"""
	while True:
		all_sql = """select t_id, quan_cheng from {tab} limit {sta}, 500000""".format(tab=tab, sta=sta)
		cur.execute(all_sql)
		results = cur.fetchall()
		if not results:
			break
		for result in results:
			t_id = result['t_id']
			quan_cheng = result['quan_cheng']
			in_redis_hash(a027_db, 'tid_name_all', t_id, quan_cheng)
		sta += len(results)
		print(sta)


if __name__ == '__main__':
	try:
		in_redis_all_tycid(setl_cur, 'tyc_jichu_chuisou')
		# in_redis_all_tycid(setl_cur, 'tyc_jichu_bj')
		# in_redis_all_tycid(setl_cur, 'tyc_jichu_gd')
		# in_redis_all_tycid(setl_cur, 'tyc_jichu_sh')
		in_redis_all_tycid(etl_cur, 'tyc_jichu_quan')
		in_redis_all_tycid(etl_cur, 'tyc_jichu_quan1')
		in_redis_all_tycid(xin_cur, 'tyc_jichu_quan')
	except:
		traceback.print_exc()
	finally:
		etl.close()
		xin.close()
