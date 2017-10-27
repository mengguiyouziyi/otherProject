import requests
import re
import time
import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet0 = book.add_sheet('jingwei', cell_overwrite_ok=True)

# all = jiexi.req()
all = [
	'北京市丰台区中核路1号',
	'北京市丰台区中核路2号',
	'北京市海淀区高梁桥斜街28号院',
	'北京市海淀区高梁桥斜街29号院',
	'北京市大兴区大兴经济开发区广平大街9号',
	'北京市大兴区大兴经济开发区广平大街10号',
	'北京市丰台区星火路9号1幢301室（园区）',
	'北京市丰台区星火路9号1幢302室（园区）',
	'北京市顺义区高丽营镇文化营村北(临空二路1号)',
	'北京市顺义区高丽营镇文化营村北(临空二路2号)',
	'北京市海淀区中关村大街18号8层03',
	'北京市海淀区中关村大街18号7层03',
]
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
}

for row, a in enumerate(all):
	url = 'http://apis.map.qq.com/jsapi?qt=poi&wd={}&pn=0&rn=10&rich_source=qipao&rich=web&nj=0&c=1&key=FBOBZ-VODWU-C7SVF-B2BDI-UK3JE-YBFUS&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb2.search_service_0'.format(a)
	print(url)
	response = requests.get(url, headers=headers)
	result = re.search(r'\{"info":.*"geoInfo": \{\}\}\}', response.text)
	if not result:
		print(a)
		continue
	result = result.group()
	print(result)