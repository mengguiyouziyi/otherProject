import pymysql
# import json
import traceback

connect = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider',
                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()

start = 0
while True:
	sql = """select * from bd_intro_bj limit %s, 20000""" % start
	start += 20000
	cursor.execute(sql)
	results = cursor.fetchall()
	if not results:
		break
	num = 0
	for result in results:
		try:
			quan_cheng = result.get('quan_cheng')
			dict = result.get('dict')
			dict_list = dict.replace("': '", '|||').replace("'},{'", '|||').replace("'}", '').split('|||')
			for i, intro in enumerate(dict_list):
				if i % 2 == 1:
					try:
						print(intro)
						result.update({'dict': intro})
						sql1 = """insert into bd_intro_bj_handled (quan_cheng, site_list, dict) VALUES (%s, %s, %s)"""
						cursor.execute(sql1, (result['quan_cheng'], result['site_list'], result['dict']))
						connect.commit()
					except:
						print(result['id'])
						traceback.print_exc()
						continue
		except:
			print(result['id'])
			traceback.print_exc()
			continue




# import pymysql
# import json
# import traceback
#
# connect = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', password='spider', db='spider',
#                           charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# cursor = connect.cursor()
#
# start = 0
# try:
# 	while True:
# 		sql = """select * from bd_intro_bj limit %s, 1000""" % start
# 		start += 1000
# 		cursor.execute(sql)
# 		results = cursor.fetchall()
# 		if start >1000:
# 			break
# 		if not results:
# 			break
# 		num = 0
# 		try:
# 			for result in results:
# 				quan_cheng = result.get('quan_cheng')
# 				dict = result.get('dict').replace('\'', '"')
# 				print(dict)
# 				dict = dict.replace('},{', ', ').replace(r'\xa0', ' ')
# 				try:
# 					dict = json.loads(dict)
# 				except:
# 					traceback.print_exc()
# 					print(result['dict'])
# 					continue
# 				intros = dict.values()
# 				try:
# 					for intro in intros:
# 						try:
# 							result.update({'dict': intro})
# 							sql1 = """insert into bd_intro_bj_handled (quan_cheng, site_list, dict) VALUES (%s, %s, %s)"""
# 							cursor.execute(sql1, (result['quan_cheng'], result['site_list'], result['dict']))
# 							connect.commit()
# 							# print(result['id'])
# 						except:
# 							print(result['id'])
# 							traceback.print_exc()
# 							continue
# 				except:
# 					print(result['id'])
# 					traceback.print_exc()
# 					continue
# 		except:
# 			traceback.print_exc()
# 			continue
# except:
# 	traceback.print_exc()
# finally:
# 	cursor.close()
# 	connect.close()
#
