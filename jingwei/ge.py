import requests
import re
import jiexi
import time
import xlwt
from traceback import print_exc

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet0 = book.add_sheet('jingwei', cell_overwrite_ok=True)


all = jiexi.req()
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
}

for row, a in enumerate(all):
	a = a.replace('辖区', '市').replace('直辖县级行政区', '')
	sheet0.write(row, 0, a)
	url = 'http://apis.map.qq.com/jsapi?qt=poi&wd={}&pn=0&rn=10&rich_source=qipao&rich=web&nj=0&c=1&key=FBOBZ-VODWU-C7SVF-B2BDI-UK3JE-YBFUS&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb2.search_service_0'.format(a)
	response = requests.get(url, headers=headers)
	# result = re.search(r'"coord":{"x":"(.*)","y":"(.*?)"}', response.text).groups()
	# try:
	result = re.search(r""""pointx": "(.*)",
			"pointy": "(.*?)",""", response.text)
	if not result:
		print(a)
		continue
	result = result.groups()
	print(a+str(result))
	sheet0.write(row, 1, result[0])
	sheet0.write(row, 2, result[1])
	time.sleep(0.5)
	# except:
	# 	print_exc()
	# 	print(a)
	# 	continue
	if row == 400:
		book.save(r'/Users/menggui/Desktop/project/otherProject/jingwei/jingwei.xls')
		continue

book.save(r'/Users/menggui/Desktop/project/otherProject/jingwei/jingwei.xls')








