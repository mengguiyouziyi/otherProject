import requests
import pymysql
from scrapy.selector import Selector
from multiprocessing import Pool

conn = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', passwd='spider', db='tyc',
                       charset="utf8",
                       use_unicode=True, cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
headers = {
	# 'host': web_site,
	'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
}


def sele():
	sql = """select * from comp_car_web_a"""
	cursor.execute(sql)
	return cursor.fetchall()


def inser(r):
	id = r.get('id', 0)
	web = r.get('website', '')
	if not web:
		return
	web_site = ('http://' + web) if 'http://' not in web and 'https://' not in web else web
	try:
		req = requests.get(web_site, headers=headers, timeout=5)
		print(req.encoding)
		status = req.status_code

		if req.encoding == 'ISO-8859-1':
			encodings = requests.utils.get_encodings_from_content(req.text)
			if encodings:
				encoding = encodings[0]
			else:
				encoding = req.apparent_encoding
			encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
		else:
			req.encoding = 'utf-8'
			encode_content = req.text

		select = Selector(text=encode_content)
		if status == 200 and req.history.__len__() == 0:
			title = select.xpath('//title/text()').extract_first()
			title = title.strip() if title else 'none'
			jump_url = ''
			flag = 1
		elif req.history.__len__() != 0:
			title = select.xpath('//title/text()').extract_first()
			title = title.strip() if title else 'none'
			jump_url = req.url
			flag = 2
		else:
			title = ''
			jump_url = ''
			flag = 3

		in_sql = """update comp_car_web_a set title=%s, jump_url=%s, flag=%s WHERE id=%s"""
		args = [title, jump_url, flag, id]
		print(args)
		cursor.execute(in_sql, args)
		conn.commit()
	except Exception as e:
		print(e)
		return


def main():
	# p = Pool(processes=6)
	results = sele()
	for r in results:
		# p.apply_async(inser(r))
		# p.close()
		# p.join()
		inser(r)
	conn.close()


if __name__ == '__main__':
	main()
