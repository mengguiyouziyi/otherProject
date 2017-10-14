"""
将所有纬度合并放入内存，存入线上库
"""

import pymysql
from outAndIn import get_redis_db, get_mysql_con, get_redis_field, _handle_str

col_dict = {'comp_id': 'only_id', 'comp_full_name': 'comp_full_name', 'comp_short_name': 'chinese_short',
            'comp_english_short': 'english_short', 'comp_credit_code': 'CreditCode',
            'comp_type': 'EconKind', 'comp_corporation': 'LegalPerson', 'comp_reg_captital': 'RegistCapi',
            'comp_create_date': 'CreateTime', 'comp_reg_authority': 'BelongOrg',
            'comp_bus_duration': 'BusinessLife',
            'comp_issue_date': 'CheckDate', 'comp_reg_status': 'RegistStatus', 'comp_provice': 'province',
            'comp_city': 'city', 'comp_district': 'district', 'comp_reg_addr': 'regaddr', 'comp_web_url': 'web_url',
            'comp_logo_tmp': 'logo_url', 'comp_phone': 'phone', 'comp_email': 'email',
            'comp_bus_range': 'BusinessScope', 'comp_introduction': 'intro', 'comp_org_type': 'OrgType',
            'comp_fax': 'fax', 'comp_contact': 'linkman'}

in_cols = col_dict.keys()  # 插入字段
in_col_str = '(' + ','.join(in_cols) + ')'  # 构建sql语句中的插入字段

sel_config = {'host': 'etl1.innotree.org',
              'port': 3308,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}

in_config = {'host': '47.95.31.183',
             'port': 3306,
             'user': 'test',
             'password': '123456',
             'db': 'innotree_data_online',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}
# 创建查询sql连接和游标
sel_con = get_mysql_con(config=sel_config)
sel_cur = sel_con.cursor()
# 创建插入sql连接和游标
in_con = get_mysql_con(config=in_config)
in_cur = in_con.cursor()
# 创建redis连接并获取所有only_id
redis_db = get_redis_db(host='a027.hb2.innotree.org')

only_ids = get_redis_field(redis_db, 'tag_only_id')

# olss = [[110, 120, 130, ....], [111, 121, 131], [112, 122, 132], ......]
olss = [[only_id.decode('utf-8') for only_id in only_ids if only_id.decode('utf-8').endswith(str(i))] for i in
        range(0, 10)]
table_list = ['comp_contactinfo_result', 'comp_intro_result', 'comp_registaddr_result',
              'comp_shortname_result', 'comp_base_result']

def a(i):
	ols = olss[i]
	in_sql = """insert into company_base_info_copy{num} {in_col} VALUES ({ss})""".format(num=i, in_col=in_col_str,
	                                                                                     ss=_handle_str(len(col_dict)))
	tables = [table + str(i) for table in table_list]
	result_mo = {}.fromkeys(col_dict.values())

	result_mo_dict = {}
	for only_id in ols:
		result_mo['only_id'] = only_id
		a = result_mo.copy()
		result_mo_dict[only_id] = a

	for table in tables:
		sel_sql = """select * from {tab} WHERE only_id in {ids}""".format(tab=table, ids=str(tuple(ols)))
		sel_cur.execute(sel_sql)
		results = sel_cur.fetchall()
		result_x = {}
		# 同一个纬度的所有列表
		for result in results:
			if not result:
				continue
			if result['score'] == 0:
				continue
			# 将每个列表中的dict本身更新
			ol = result['only_id']
			result_x.update(result_mo_dict[ol])
			result_x.update(result)
			for k, v in result_x.items():
				if v in ['', '未公开']:
					result_x.update({k: None})
			result_mo_dict[ol].update(result_x)

	value_list = [[result_mo[col_dict[in_col]] for in_col in in_cols] for result_mo in result_mo_dict.values() if
	              result_mo['comp_full_name']]
	values = []
	for i, value in enumerate(value_list):
		i += 1
		print(i)
		values.append(value)
		if len(values) == 3000:
			in_cur.executemany(in_sql, values)
			in_con.commit()
			values.clear()
		else:
			continue
	in_cur.executemany(in_sql, values)
	in_con.commit()

try:
	# for i in [0,1,5,6,9,2]:
	a(9)
finally:
	sel_con.close()
	in_con.close()
