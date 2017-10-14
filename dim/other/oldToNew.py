import re
import pymysql
import os
import sys

# config = {'host': '47.95.31.183',
#              'port': 3306,
#              'user': 'test',
#              'password': '123456',
#              # 'db': 'innotree_data_online',
#              'charset': 'utf8',
#              'cursorclass': pymysql.cursors.DictCursor}
# mysql = pymysql.connect(**config)
# cursor = mysql.cursor()
# path = "/Users/menggui/Desktop/newchain/dianzixinxi.jsp"
dir_path = "/Users/menggui/Desktop/newchain/"
paths = [f for f in os.listdir(dir_path)]

for path in paths:
	with open(path, 'r') as f:
		x = f.read()
		co = re.compile(r'\<a href="/inno/company/(\d+?)\.html" target="view_window" class="in_se_a03"\>(.+?)\</a\>')
		se = re.findall(co, x)
		print(se)