"""
每次查询一条
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

in_cols = col_dict.keys()
in_col_str = '(' + ','.join(in_cols) + ')'
# in_sql = """insert into company_base_info {in_col} VALUES ({ss})""".format(in_col=in_col_str,
#                                                                            ss=_handle_str(len(col_dict)))
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
             'db': 'innotree_data',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}

sel_con = get_mysql_con(config=sel_config)
sel_cur = sel_con.cursor()

in_con = get_mysql_con(config=in_config)
in_cur = in_con.cursor()

redis_db = get_redis_db(host='a027.hb2.innotree.org')

only_ids = get_redis_field(redis_db, '200w_only_id')
olss = [[only_id.decode('utf-8') for only_id in only_ids if only_id.decode('utf-8').endswith(str(i))] for i in
        range(0, 10)]
table_list = ['comp_base_result', 'comp_contactinfo_result', 'comp_intro_result', 'comp_registaddr_result', 'comp_shortname_result']
try:
	for i, ols in enumerate(olss):
		in_sql = """insert into company_base_info{num} {in_col} VALUES ({ss})""".format(num=i, in_col=in_col_str,
		                                                                           ss=_handle_str(len(col_dict)))
		result_list = []
		tables = [table + str(i) for table in table_list]
		for j, ol in enumerate(ols):
			print(ol)
			result_mo = {sel_col: None for sel_col in col_dict.values()}
			s = 0
			for table in tables:
				sel_sql = """select * from {tab} WHERE only_id = %s""".format(tab=table)
				sel_cur.execute(sel_sql, [str(ol)])
				result = sel_cur.fetchone()
				if not result:
					s += 1
					continue
				if result['score'] == 0:
					s += 1
					continue
				result.get('comp_create_date')
				result_mo.update(result)
			if s == 5:
				continue
			# print(result_mo)
			#
			# values = [result_mo[col_dict[in_col]] for in_col in in_cols]
			# print(values)
			# print(in_sql)
			# in_cur.execute(in_sql, values)
			# in_con.commit()

			result_list.append(result_mo)
			print(i + j)

		value_list = [[result[col_dict[in_col]] for in_col in in_cols] for result in result_list]
		in_cur.executemany(in_sql, value_list)
		in_con.commit()
finally:
	sel_con.close()
	in_con.close()
