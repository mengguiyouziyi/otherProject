import requests
import re
import pymysql
# import jiexi
import time
import xlwt
from traceback import print_exc

connect = pymysql.connect(host='112.126.86.232', port=3306, user='xiaoenzhen', password='SDyHh47J52dtELAk', db='innotree_data_online',
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cur = connect.cursor()

sql = """select area_id, area_name from dim_area"""

cur.execute(sql)
results = cur.fetchall()



book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet0 = book.add_sheet('jingwei', cell_overwrite_ok=True)


headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
}

for row, r in enumerate(results):
	b = r['area_id']
	a = r['area_name']
	sheet0.write(row, 0, b)
	a = a.replace('辖区', '市').replace('直辖县级行政区', '')
	sheet0.write(row, 1, a)
	url = 'http://apis.map.qq.com/jsapi?qt=poi&wd={}&pn=0&rn=10&rich_source=qipao&rich=web&nj=0&c=1&key=FBOBZ-VODWU-C7SVF-B2BDI-UK3JE-YBFUS&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb2.search_service_0'.format(a)
	response = requests.get(url, headers=headers)
	# result = re.search(r'"coord":{"x":"(.*)","y":"(.*?)"}', response.text).groups()
	# try:
	re_org = re.search(r""""pointx": "(.*)",
			"pointy": "(.*?)",""", response.text)
	if not re_org:
		print(a)
		continue
	result_org = re_org.groups()
	print(a+str(result_org))
	sheet0.write(row, 2, result_org[0])
	sheet0.write(row, 3, result_org[1])
	time.sleep(0.5)
	# except:
	# 	print_exc()
	# 	print(a)
	# 	continue
	if row == 400:
		book.save(r'/Users/menggui/Desktop/project/otherProject/jingwei/jingwei.xls')
		continue

book.save(r'/Users/menggui/Desktop/project/otherProject/jingwei/jingwei.xls')








