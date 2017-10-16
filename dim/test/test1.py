#~~~~~~~~~~~~~~~~~ 测试 select_db() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
from dim.utility.tools import get_redis_db, get_mysql_con, get_redis_field, _handle_str
from dim.utility.info import a024, a027, etl_config, xin_config, online_config

a027_db = get_redis_db(a027)
# a024_db = get_redis_db(a024)

# etl = pymysql.connect(**etl_config)
# etl.select_db('tyc')
# etl_cur = etl.cursor()

# xin = pymysql.connect(**xin_config)
# xin.select_db('tianyancha')
# xin_cur = xin.cursor()

online = pymysql.connect(**online_config)
online.select_db('innotree_data_online')
online_cur = online.cursor()

sql1 = """select * from company_base_info limit 2"""
online_cur.execute(sql1)
r1 = online_cur.fetchall()
print(r1)

online.select_db('innotree_data')
no_cur = online.cursor()

sql2 = """select * from company_base_info limit 2"""
no_cur.execute(sql2)
r2 = no_cur.fetchall()
print(r2)

#~~~~~~~~~~~~~~~~~ 结论：可以重复选择db ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


























################### 测试多进程 ###########################################################################################
# import multiprocessing
# from multiprocessing import Pool
#
#
# def readAndSet():
# 	num = 0
# 	print(multiprocessing.current_process().name + " " + str(num))
# 	# print(multiprocessing.current_process().name)
#
# 	# while num < 5:
# 	# 	print(multiprocessing.current_process().name + " " + str(num))
# 	# 	num = num + 1
#
#
# pool = Pool()
# # for num in range(4):
# # 	pool.apply_async(readAndSet, args=(num,))
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.close()
# pool.join()
# print("程序运行结束")
#
#
# import multiprocessing
#
# num = 0
#
# def readAndSet():
#     global num
#     while num < 5:
#         print(multiprocessing.current_process().name + " "+str(num))
#         num = num + 1
#
# cpus = multiprocessing.cpu_count()
# print(cpus)
# pool = multiprocessing.Pool(processes = 2)
# pool.apply_async(readAndSet)
# pool.apply_async(readAndSet)
# pool.close()
# pool.join()
# print("程序运行结束")
##############################################################################################################
