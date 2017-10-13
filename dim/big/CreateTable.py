# coding:utf-8
"""

"""
import pymysql
import traceback


def _sqlObj(db):
	"""
	连接数据库并获取游标
	参数：数据库
	"""
	connect = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', password='spider', db=db,
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = connect.cursor()
	return connect, cursor


def createTable(create_table):
	"""

	:return:
	"""
	table = create_table['table']
	colum_list = create_table['colum_list']
	if _checkTableExists(table['name']):
		return
	sql1 = """CREATE TABLE `{tab}` (
		  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',""".format(tab=table['name'])
	sql2 = """`{name}` {type_size} {default} NULL COMMENT '{comment}',"""
	sql3 = """`load_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
		  PRIMARY KEY (`id`)
		) ENGINE=INNODB DEFAULT CHARSET=utf8 COMMENT='{comment}'
	""".format(comment=table['comment'])
	colum_plus = ''
	for colum in colum_list:
		sql_x = sql2.format(name=colum['name'], type_size=colum['type_size'], default=colum['default'], comment=colum['comment'])
		colum_plus += sql_x
	print(colum_plus)
	sql = sql1 + colum_plus + sql3
	print(sql)

	con, cur = _sqlObj('spider_dim')
	try:
		cur.execute(sql)
		con.commit()
	except:
		traceback.print_exc()
	finally:
		con.close()


def _checkTableExists(tablename):
	con, dbcur = _sqlObj('spider_dim')
	sql = """
        SELECT *
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename)
	dbcur.execute(sql)

	if dbcur.fetchone():
		dbcur.close()
		return True

	dbcur.close()
	return False


def main(create_table_list):
	for create_table in create_table_list:
		createTable(create_table)


if __name__ == '__main__':
	"""
	用来测试，要给真实数据
	"""
	a = [
		{'table': {'name': '', 'comment': ''},
		 'colum_list': [
			 {'name': '', 'type_size': '', 'default': '', 'comment': ''},
			 {'name': '', 'type_size': '', 'default': '', 'comment': ''}
		 ]}
	]
	for b in a:
		createTable(b)
