# -*- coding: utf-8 -*-
import xlwt
import xlrd
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='3646287', db='spider',
                       charset="utf8", use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()


def searc():
	xlsfile = r"/Users/menggui/Downloads/search.xls"  # 打开指定路径中的xls文件
	books = xlrd.open_workbook(xlsfile)  # 得到Excel文件的book对象，实例化对象
	sheet0 = books.sheet_by_index(0)  # 通过sheet索引获得sheet对象
	nrows = sheet0.nrows  # 获取行总数
	comm = [sheet0.row_values(i)[2] for i in range(1, nrows)]


	# sql = """select * from qichacha_search where Name=%s"""
	sql = """select * from qichacha_changerecords where KeyNo=%s"""


	book = xlwt.Workbook(encoding='utf-8', style_compression=0)
	sheet = book.add_sheet('search', cell_overwrite_ok=True)

	a(comm, sql, sheet)

	book.save(r'/Users/menggui/Downloads/1111.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错


def a(comm, sql, sheet):
	x = 0
	for row, c in enumerate(comm):
		cursor.execute(sql, c)
		result = cursor.fetchone()
		if not result:
			continue
		if result and x == 0:
			for col, k in enumerate(result.keys()):
				sheet.write(row - 1, col, k)
			x += 1

		for col, v in enumerate(result.values()):
			sheet.write(row + 1, col, v)
		print(row)


if __name__ == '__main__':
	searc()
