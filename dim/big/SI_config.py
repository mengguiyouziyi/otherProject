# coding:utf-8
"""
项目读取配置文件
"""
##########################################################################################
"""
搜索源数据表，插入纬度数据表，只需传入 
sel_columns(搜索字段)，sel_table(搜索表名), db(搜索数据库)，
inser_table(插入表名)，inser_columns(插入字段) 即可
"""
sel_inser_list = [
	# 机构jigou
	# dw_online.si_jiben 有数据 不知道有没有一直更新
	# {'sel_columns': 'company_full_name,s_id,logo,company_abbreviation,company_eng_abbreviation,web,establishment_time,capital_type,organization_form,VC,managed_capital,registered_area,corporate_headquarters,keep_on_record,registration_number,describe,filing_time,p_id',
	#  'sel_table': 'si_jiben', 'db': 'dw_online',
	#  'inser_table': 'jigou_base_smt',
	#  'inser_columns': '(comp_full_name,s_id,logo,company_abbreviation,company_eng_abbreviation,web,establishment_time,capital_type,organization_form,VC,managed_capital,registered_area,corporate_headquarters,keep_on_record,registration_number,describe,filing_time,p_id)'},


# base 补全
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, zuzhijigou_daima, nashui_shibie, gongshang_hao',
	# 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	# 'inser_table': 'comp_basebuquan_tyc',
	# 'inser_columns': '(comp_full_name, zuzhijigou_daima, nashui_shibie, gongshang_hao)'},


	# 新实例增量
	# base
	# tianyancha.tyc_jichu_quan   8228753 8279076
	# {'sel_columns': 'quan_cheng, tongyi_xinyong, qiye_leixing, fa_ren, zhuce_ziben, zhuce_shijian, dengji_jiguan, yingye_nianxian, jingying_zhuangtai, hezhun_riqi, jingying_fanwei',
	# 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	# 'inser_table': 'comp_base_tyc',
	# 'inser_columns': '(comp_full_name, CreditCode, EconKind, LegalPerson, RegistCapi, CreateTime, BelongOrg, BusinessLife, RegistStatus, CheckDate, BusinessScope)'},

	# website
	# tianyancha.tyc_jichu_quan 8228753
	# {'sel_columns': 'quan_cheng, w_eb', 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	#  'inser_table': 'comp_web_tyc', 'inser_columns': '(comp_full_name, web_url)'},

	# logo
	# tianyancha.tyc_jichu_quan 8228753
	# {'sel_columns': 'quan_cheng, logo', 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	#  'inser_table': 'comp_logo_tyc', 'inser_columns': '(comp_full_name, logo_url)'},

	# registaddr
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, zhuce_dizhi', 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	#  'inser_table': 'comp_registaddr_tyc', 'inser_columns': '(comp_full_name, regaddr)'},

	# office
	# tianyancha.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, a_ddress', 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	#  'inser_table': 'comp_officeaddr_tyc', 'inser_columns': '(comp_full_name, offaddr)'},

	# contact
	# tianyancha.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, p_hone, e_mail', 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	#  'inser_table': 'comp_contactinfo_tyc', 'inser_columns': '(comp_full_name, phone, email)'},

	# intro
	# tianyancha.tyc_jichu_quan  8230939
	# {'sel_columns': 'quan_cheng, c_desc', 'sel_table': 'tyc_jichu_quan', 'db': 'tianyancha',
	#  'inser_table': 'comp_intro_tyc', 'inser_columns': '(comp_full_name, intro)'},




	# base
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, tongyi_xinyong, qiye_leixing, fa_ren, zhuce_ziben, zhuce_shijian, dengji_jiguan, yingye_nianxian, jingying_zhuangtai, hezhun_riqi, jingying_fanwei',
	# 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	# 'inser_table': 'comp_base_tyc',
	# 'inser_columns': '(comp_full_name, CreditCode, EconKind, LegalPerson, RegistCapi, CreateTime, BelongOrg, BusinessLife, RegistStatus, CheckDate, BusinessScope)'},

	# website
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, w_eb', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_web_tyc', 'inser_columns': '(comp_full_name, web_url)'},

	# logo
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, logo', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_logo_tyc', 'inser_columns': '(comp_full_name, logo_url)'},

	# registaddr
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, zhuce_dizhi', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_registaddr_tyc', 'inser_columns': '(comp_full_name, regaddr)'},

	# officeaddr
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, a_ddress', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_officeaddr_tyc', 'inser_columns': '(comp_full_name, offaddr)'},

	# contactinfo
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, p_hone, e_mail', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_contactinfo_tyc', 'inser_columns': '(comp_full_name, phone, email)'},

	# intro
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, c_desc', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_intro_tyc', 'inser_columns': '(comp_full_name, intro)'},
]
##########################################################################################
"""
创建纬度表，需要输入 表名、表名描述，字段名、字段类型及长度、是否默认为null、字段描述
"""
create_table_list = [

]
##########################################################################################
