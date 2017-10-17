"""
将所有 t_id：comp_full_name 放入 t_id_name_all 中
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

# a027_db = get_redis_db(a027)
#
# etl = pymysql.connect(**etl_config)
#
# etl.select_db('spider')
# spi_cur = etl.cursor()

xin = pymysql.connect(**xin_config)
xin.select_db('tianyancha')
xin_cur = xin.cursor()


def in_redis_all_tycid(cur, tab, sta=0):
	"""
	将全量t_id入到redis总量key中
	:return:
	"""
	print('~~~~~~~~~~~~~~~'+str(tab)+'~~~~~~~~~~~~~~~~~')
	while True:
		all_sql = """select t_id, quan_cheng from {tab} limit {sta}, 500000""".format(tab=tab, sta=sta)
		cur.execute(all_sql)
		results = cur.fetchall()
		if not results:
			break
		for result in results:
			t_id = result['t_id']
			quan_cheng = result['quan_cheng']
			in_redis_hash(a027_db, 't_id_name_all', t_id, quan_cheng)
		sta += len(results)
		print(sta)


if __name__ == '__main__':
	try:
		# in_redis_all_tycid(spi_cur, 'tyc_jichu_chuisou')
		# # in_redis_all_tycid(spi_cur, 'tyc_jichu_bj')
		# # in_redis_all_tycid(spi_cur, 'tyc_jichu_gd')
		# # in_redis_all_tycid(spi_cur, 'tyc_jichu_sh')
		#
		# # 需要在这里来选择数据库，
		# etl.select_db('tyc')
		# tyc_cur = etl.cursor()
		# in_redis_all_tycid(tyc_cur, 'tyc_jichu_quan')
		# in_redis_all_tycid(tyc_cur, 'tyc_jichu_quan1')

		in_redis_all_tycid(xin_cur, 'tyc_jichu_quan')
	except:
		traceback.print_exc()
	finally:
		etl.close()
		xin.close()
