"""
将所有纬度合并放入内存，存入线上库
"""
import os
import sys
import pymysql
from math import ceil
from dim.utility.tools import get_redis_db, get_mysql_con, get_redis_field, _handle_str
from dim.utility.info import a024, a027, etl_config, xin_config, online_config

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

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

table_list = ['comp_contactinfo_result', 'comp_intro_result', 'comp_registaddr_result',
              'comp_shortname_result', 'comp_base_result']

a027_db = get_redis_db(a027)
# a024_db = get_redis_db(a024)

etl = pymysql.connect(**etl_config)
etl.select_db('dimension_result')
result_cur = etl.cursor()

# xin = pymysql.connect(**xin_config)
# xin.select_db('tianyancha')
# xin_cur = xin.cursor()

online = pymysql.connect(**online_config)
online.select_db('innotree_data')
online_cur = online.cursor()


def get_ids(re_key):
	"""
	一次性获取 re_key 中的全量 only_id
	:param re_key:
	:return:
	"""
	only_ids = get_redis_field(a027_db, re_key)
	ols = [only_id.decode('utf-8') for only_id in only_ids]
	return ols


def together(oo, i):
	"""
	五个纬度 汇总
	:param ols: 某一尾号的 only_id 列表
	:param i: 尾号-表
	:return:
	"""
	in_cols = col_dict.keys()  # 插入字段
	in_col_str = '(' + ','.join(in_cols) + ')'  # 构建sql语句中的插入字段
	in_sql = """insert into company_base_info_copy{num} {in_col} VALUES ({ss})""".format(num=i, in_col=in_col_str,
	                                                                                     ss=_handle_str(len(col_dict)))
	tables = [table + str(i) for table in table_list]
	result_mo = {}.fromkeys(col_dict.values())

	result_mo_dict = {}
	for only_id in ols:
		result_mo['only_id'] = only_id
		result_mo_dict[only_id] = result_mo.copy()

	for table in tables:
		sel_sql = """select * from {tab} WHERE only_id in {ids}""".format(tab=table, ids=str(tuple(oo)))
		result_cur.execute(sel_sql)
		results = result_cur.fetchall()
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
	for j, value in enumerate(value_list):
		j += 1
		print(j)
		values.append(value)
		if len(values) == 3000:
			online_cur.executemany(in_sql, values)
			online_cur.commit()
			values.clear()
		else:
			continue
	online_cur.executemany(in_sql, values)
	online_cur.commit()


if __name__ == '__main__':
	try:
		for i in range(10):
			re_key = 'id_name_all_{num}'.format(num=i)
			ols = get_ids(re_key)
			ol_list = [ols[100000 * s: 100000 * (s + 1)] for s in range(ceil(len(ols) / 100000))]
			for oo in ol_list:
				together(oo, i)
	finally:
		etl.close()
		online.close()
