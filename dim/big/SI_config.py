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
	# app
	# spider.wandoujia
	{
		'sel_columns': 'a_kaifa, a_logo, a_bao, a_name, a_xia, a_size, a_ban, a_jietu, a_desc, a_fen, a_tag, a_update, a_hap, a_ping, a_all',
		'sel_table': 'wandoujia', 'db': 'spider',
		'inser_table': 'item_app_wandoujia',
		'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, down_num, size, version, pictures, description, category, tags, update_time, good_comm_rate, comm_num, also_likes)'},

	# spider.xiaomi
	{'sel_columns': 'a_kaifa, a_logo, a_bao, a_name, a_size, a_ban, a_jietu, a_desc, a_fen, a_update, a_ping, a_all',
	 'sel_table': 'xiaomi', 'db': 'spider',
	 'inser_table': 'item_app_xiaomi',
	 'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, size, version, pictures, description, category, update_time, comm_num, also_likes)'},

	# spider.360app
	{
		'sel_columns': 'auth, pic, pac_name, soft_name, is_official, down_num, score, apk_size, version, overview, des, app_cat, tag, update_time, comm_num, best_num, good_num, bad_num, likes',
		'sel_table': 'app_360_update', 'db': 'spider',
		'inser_table': 'item_app_360app',
		'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, is_gov, down_num, score, size, version, pictures, description, category, tags, update_time, comm_num, good_comm_num, mid_comm_num, bad_comm_num, also_likes)'},

	# # spider.hw_app
	{
		'sel_columns': 'auth, logo_url, pname, soft_name, down_num, soft_score, soft_size, version, pic_url, des, create_date, comm_num',
		'sel_table': 'app_hw_update', 'db': 'spider',
		'inser_table': 'item_app_huawei',
		'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, down_num, score, size, version, pictures, description, update_time, comm_num)'},
	#
	# # spider.yingyb
	{
		'sel_columns': 'authorName, iconUrl, pkgName, appName, isOfficial, appDownCount, averageRating, fileSize, versionName, images, description, categoryName, apkPublishTime, ratingCount, sameList',
		'sel_table': 'app_yyb_update', 'db': 'spider',
		'inser_table': 'item_app_yingyongbao',
		'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, is_gov, down_num, score, size, version, pictures, description, category, update_time, comm_num, same_develop)'},

	# intro
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'comp_name, intro', 'sel_table': 'jianjie_shunqi_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_shunqi', 'inser_columns': '(comp_full_name, intro)'},

	# {'sel_columns': 'comp_name, intro', 'sel_table': 'jianjie_114_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_114', 'inser_columns': '(comp_full_name, intro)'},
	#
	# {'sel_columns': 'comp_name, intro', 'sel_table': 'jianjie_huangye88_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_huangye88', 'inser_columns': '(comp_full_name, intro)'},
	#
	# {'sel_columns': 'comp_name, intro', 'sel_table': 'jianjie_wuyou_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_wuyou', 'inser_columns': '(comp_full_name, intro)'},

	# {'sel_columns': 'comp_name, intro', 'sel_table': 'jianjie_zhizao_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_zhongguozhizao', 'inser_columns': '(comp_full_name, intro)'},

	# spider.hw_app
	# {
	# 	'sel_columns': 'auth, logo_url, pname, soft_name, down_num, soft_score, soft_size, version, pic_url, des, create_date, comm_num',
	# 	'sel_table': 'hw_app', 'db': 'spider',
	# 	'inser_table': 'item_app_huawei',
	# 	'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, down_num, score, size, version, pictures, description, update_time, comm_num)'},

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
	# tianyancha.tyc_jichu_quan   8228753 8279076 8288248
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
