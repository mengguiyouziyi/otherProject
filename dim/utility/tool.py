import pymysql
import os
import time
import logging
import redis

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_redis_db(host, port=6379, db=0):
	"""
	获取redis实例连接
	:param host:
	:param port:
	:param db:
	:return:
	"""
	pool = redis.ConnectionPool(host=host, port=port, db=db)
	redis_db = redis.StrictRedis(connection_pool=pool, decode_responses=True)
	return redis_db


def get_redis_field(redis_db, key):
	"""
	获取redis key中的所有field
	:param redis_db:
	:param key:
	:return:
	"""
	return redis_db.hkeys(key)


def in_redis_hash(redis_db, key, field, value):
	"""
	向redis中插入hash数据
	:param redis_db:
	:param key:
	:param value:
	:param field:
	:return:
	"""
	redis_db.hmset(key, {field: value})


def get_redis_hash(redis_db, key, field):
	"""
	返回redis中的hash值
	:param redis_db:
	:param key:
	:param field:
	:return:
	"""
	return redis_db.hget(key, field)


def in_redis_string(redis_db, key, value):
	"""
	向redis中插入string数据
	:param redis_db:
	:param key:
	:param value:
	:return:
	"""
	redis_db.set(key, value)


def get_redis_string(redis_db, key):
	"""
	返回redis中的string值
	:param redis_db:
	:param key:
	:return:
	"""
	return redis_db.get(key)


def get_mysql_con(config):
	"""
	获取mysql实例连接（尚未设置db）
	:param config:
	:return:
	"""
	connect = pymysql.connect(**config)
	return connect


def _handle_str(num):
	"""
	内部函数，只在insert语句中使用
	根据插入字段数量来构造sql语句的（%s, %s ....）
	:param num: 插入字段数量
	:return: sql的value字符串
	"""
	x = "%s"
	for i in range(num - 1):
		x += ", %s"
	return x


def get_col_str(con, db, tab):
	"""
	获取当前表格的字段的字符串
	:param con: 连接
	:param db: 表所在的库
	:param tab: 要获取字段字符串的表
	:return:
	"""
	sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{tab}' and table_schema = '{db}'""".format(
		tab=tab, db=db)
	cur = con.cursor()
	cur.execute(sql)
	results = cur.fetchall()
	columns_str = results[0]['group_concat(column_name)']
	return columns_str


def sel_fun(sel_con, sel_db, sel_tab, con_value, sel_col='*', start=0, lim=500000, where=None, condition='only_id'):
	"""
	查询表并返回元素为dict的结果集
	:param sel_con: 查询表所在的连接
	:param sel_db: 查询表所在的数据库
	:param sel_tab: 查询表
	:param sel_col: 需要查询的字段
	:param start:
	:param limi:
	:return:
	"""
	sel_con.select_db(db=sel_db)
	cur = sel_con.cursor()
	if not where:
		sql = """select {col} from {tab} limit {start}, {limit}""".format(col=sel_col, tab=sel_tab, start=start,
		                                                                  limit=lim)
		cur.execute(sql)
	else:
		sql = """select {col} from {tab} WHERE {condition} = %s limit {start}, {limit}""".format(col=sel_col,
		                                                                                         tab=sel_tab,
		                                                                                         condition=condition,
		                                                                                         start=start,
		                                                                                         limit=lim)
		cur.execute(sql, con_value)

	return cur.fetchall()


def in_many_fun(in_con, in_db, in_tab, value_list):
	"""
	插入多条sql语句
	:param in_con: 连接
	:param in_db: 要插入表所在的库
	:param in_tab: 要插入数据的表
	:param value_list: 字段对应的值
	:return:
	"""
	in_con.select_db(in_db)
	col_str = get_col_str(in_con, in_db, in_tab)
	col_list = col_str.split(',')
	col_str_part = ''.join(col_list[1:-1])
	in_sql = """insert into {tab} ({col}) VALUES ({val})""".format(tab=in_tab, col=col_str_part,
	                                                               val=_handle_str(len(col_list)))
	in_cur = in_con.cursor()
	in_cur.executemany(in_sql, value_list)
	in_con.commit()


def loop_in_fun(in_con, in_db, in_tab, results):
	"""
	向mysql对应实体的对应数据库的对应表中循环插入数据
	数据的值具有不确定性
	情况一：完全拷贝，字段可能同名
	情况二：部分拷贝，字段可能同名
	情况三：部分拷贝，但是有的字段在源表中不存在
	情况四：
	:param in_con:
	:param in_db:
	:param in_tab:
	:param values: 要插入的值的列表（result中的值列表）
	:return:
	"""
	# for result in results:
	# 	values = dict_to_list(result, con, db, tab)
	# 	value_list = []
	# 	value_list.append(values)
	# 	if len(value_list) == 50000:
	# 		in_many_fun(in_con, in_db, in_tab, value_list)
	# 	else:
	# 		in_many_fun(in_con, in_db, in_tab, value_list)
	pass


def loop_sel_fun(sel_con, sel_db, sel_tab, in_con, in_db, in_tab, values, update_dict={}, sel_col='*', start=0,
                 lim=500000):
	# while True:
	# 	if not results:
	# 		time.sleep(1200)
	# 		continue
	# 	for result in results:
	# 		result = add_values(update_dict)
	#
	# 	loop_in_fun(in_con, in_db, in_tab, values)
	pass


def dict_to_list(result, con, db, tab):
	"""
	将查询结果dict获取按照次序排列的值的列表
	:param result:
	:param con:
	:param db:
	:param tab:
	:return:
	"""
	col_str = get_col_str(con, db, tab)
	col_list = [col.strip() for col in col_str.split(',')]
	return [result[col] for col in col_list]


def add_values(result, update_dict):
	"""
	从redis中或者其他表中获取的数据，更新到result字典中
	:param result:
	:param kwargs: 要更新的字典，如{'col1':'value1', 'col2':'value2'....}
	:return:
	"""
	return result.update(update_dict)


# # 用于搜索的mysql连接
# sel_con = get_mysql_con(sel_config)
#
# # 用于插入的mysql连接
# in_con = get_mysql_con(config=in_config)
# in_col_str = get_col_str(in_con, in_tab)
#
#
#
# while True:
# 	results = _sel_fun(sel_con, sel_db, sel_tab, sel_col=sel_col, start=start, lim=lim)
# 	if not results:
# 		return
# 	value_list = []
# 	for result in results:
# 		start += 1
# 		print(start)
# 		if has_redis:
# 			comp_full_name = _get_redis(redis_db=redis_db, key=result['t_id'], field=field, model=)
# 			result['comp_full_name'] = comp_full_name if comp_full_name else ''
# 		columns_list = columns.split(',')
# 		values = [result[column] for column in columns_list]
# 		value_list.append(values)
# 		if len(value_list) == 5000:
# 			_in_many_fun(insert_con, table_in, value_list)
# 			print('done')
# 			value_list.clear()
# 		else:
# 			continue
# 	insertManyFun(insert_con, table_in, value_list)


# class OutAndIn(object):
# 	def __init__(self, has_redis, sel_config, sel_db, sel_tab, sel_col, start, lim, in_config, in_db, in_tab):
# 		self.has_redis = has_redis if has_redis else False
# 		self.sel_config = sel_config
# 		self.sel_db = sel_db if sel_db else 'tyc'
# 		self.sel_tab = sel_tab if sel_tab else 'tyc_jichu_quan'
#
# 	def main(self):
# 		pass


if __name__ == '__main__':
	mysql_config1 = {'host': 'etl1.innotree.org',
	                 'port': 3308,
	                 'user': 'spider',
	                 'password': 'spider',
	                 # 'db': 'spider_dim',
	                 'charset': 'utf8',
	                 'cursorclass': pymysql.cursors.DictCursor}

	mysql_config2 = {'host': '10.252.0.52',
	                 'port': 3306,
	                 'user': 'etl_tmp',
	                 'password': 'UsF4z5HE771KQpra',
	                 # 'db': 'tianyancha',
	                 'charset': 'utf8',
	                 'cursorclass': pymysql.cursors.DictCursor}

	QUEUE_REDIS_HOST = ''
	QUEUE_REDIS_PORT = 6379
