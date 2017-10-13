import pymysql


def is_chinese(uchar):
	"""判断一个unicode是否是汉字"""
	if uchar >= u'u4e00' and uchar <= u'u9fa5':
		return True
	else:
		return False


def is_number(uchar):
	"""判断一个unicode是否是数字"""
	if uchar >= u'u0030' and uchar <= u'u0039':
		return True
	else:
		return False


def is_alphabet(uchar):
	"""判断一个unicode是否是英文字母"""
	if (uchar >= u'u0041' and uchar <= u'u005a') or (uchar >= u'u0061' and uchar <= u'u007a'):
		return True
	else:
		return False


def is_other(uchar):
	"""判断是否非汉字，数字和英文字符"""
	if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
		return True
	else:
		return False

def _handle_str(num):
	"""
	根据插入字段数量来构造sql语句的（%s, %s ....）
	:param num: 插入字段数量
	:return: sql的value字符串
	"""
	x = "%s"
	for i in range(num - 1):
		x += ", %s"
	return x


def get_mysql_con(config):
	"""
	获取mysql实例连接（尚未设置db）
	:param config:
	:return:
	"""
	connect = pymysql.connect(**config)
	return connect


def sel_fun(sel_con, sel_db, sel_tab, sel_col='*', start=0, lim=500000):
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
	sql = """select {col} from {tab} limit {start}, {limit}""".format(col=sel_col, tab=sel_tab, start=start,
	                                                                  limit=lim)
	cur = sel_con.cursor()
	cur.execute(sql)
	return cur.fetchall()


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


def name_same(result):
	"""
	全称简称完全相同
	:return:
	"""
	if result['comp_full_name'] == result['chinese_short']:
		result['score'] = 0
	else:
		result['score'] = 10


def too_long(result):
	"""
	简称太长的
	:return:
	"""
	short = result['chinese_short']


def en_to_ch():
	"""
	英文简称完全中文的放到中文简称中
	:return:
	"""
	pass


def ch_to_en():
	"""
	中文简称完全英文的放到英文简称中
	:return:
	"""
	pass


def split_ch_en():
	"""
	切分中英文简称
	:return:
	"""
	pass


def move_right():
	"""
	将切分完的中英文简称放到正确位置
	:return:
	"""
	pass


def del_city():
	# no
	pass


def contain_all():
	"""
	针对拉钩，简称分词之后要完全出现在全称中，会刷掉一部分有用数据
	:return:
	"""
	pass


if __name__ == '__main__':
	mysql_config = {'host': 'etl1.innotree.org',
	                'port': 3308,
	                'user': 'spider',
	                'password': 'spider',
	                # 'db': 'spider_dim',
	                'charset': 'utf8',
	                'cursorclass': pymysql.cursors.DictCursor}
	sel_db = 'dimension_sum'
	sel_tab = 'comp_shortname_sum0'
	sel_con = get_mysql_con(**mysql_config)
	results = sel_fun(sel_con, sel_db, sel_tab)
	for result in results:
		result = name_same(result)




