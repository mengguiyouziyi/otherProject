# coding:utf-8
"""
项目总配置文件
"""
##########################################################################################
"""
搜索源数据表，插入纬度数据表，只需传入 
sel_columns(搜索字段)，sel_table(搜索表名), db(搜索数据库)，
inser_table(插入表名)，inser_columns(插入字段) 即可
"""
sel_inser_list = [
	# 基金
	# spider.si_jijin_detail
	# {'sel_columns': 'zhong_quan,s_id,g_id,zhong_jian,ying_jian,guanli_jigou,zhengfu_flag,chengli_time,zong_bu,ziben_type,zuzhi_xingshi,jijin_type,muji_statue,bei_an,shenbao_statue,de_sc,moditme',
	#  'sel_table': 'si_jijin_detail', 'db': 'spider',
	#  'inser_table': 'fund_base_smt',
	#  'inser_columns': '(comp_full_name,s_id,g_id,zhong_jian,ying_jian,guanli_jigou,zhengfu_flag,chengli_time,zong_bu,ziben_type,zuzhi_xingshi,jijin_type,muji_statue,bei_an,shenbao_statue,de_sc,moditme)'},

	# 机构jigou
	# dw_online.si_jiben 有数据 不知道有没有一直更新
	{'sel_columns': 'company_full_name,s_id,logo,company_abbreviation,company_eng_abbreviation,web,establishment_time,capital_type,organization_form,VC,managed_capital,registered_area,corporate_headquarters,keep_on_record,registration_number,describe,filing_time,p_id',
	 'sel_table': 'si_jiben', 'db': 'dw_online',
	 'inser_table': 'jigou_base_smt',
	 'inser_columns': '(comp_full_name,s_id,logo,company_abbreviation,company_eng_abbreviation,web,establishment_time,capital_type,organization_form,VC,managed_capital,registered_area,corporate_headquarters,keep_on_record,registration_number,describe,filing_time,p_id)'},

	# 退出事件
	# dw_online.si_jiben 有数据 不知道有没有一直更新
	# {'sel_columns': 'company_full_name,s_id,logo,company_abbreviation,company_eng_abbreviation,web,establishment_time,capital_type,organization_form,VC,managed_capital,registered_area,corporate_headquarters,keep_on_record,registration_number,describe,filing_time,p_id',
	#  'sel_table': 'si_jiben', 'db': 'dw_online',
	#  'inser_table': 'jigou_base_smt',
	#  'inser_columns': '(comp_full_name,s_id,logo,company_abbreviation,company_eng_abbreviation,web,establishment_time,capital_type,organization_form,VC,managed_capital,registered_area,corporate_headquarters,keep_on_record,registration_number,describe,filing_time,p_id)'},


	# 项目item

	# 作者，App图标，App包名，App名称，是否官方，下载量，评分，大小，版本，截图，描述，分类，标签，更新时间，好评率，评论数，好评数，中坪数，差评数，同一开发者，下载的人还喜欢
	# spider.wandoujia
	# {
	# 	'sel_columns': 'a_kaifa, a_logo, a_bao, a_name, a_xia, a_size, a_ban, a_jietu, a_desc, a_fen, a_tag, a_update, a_hap, a_ping, a_all',
	# 	'sel_table': 'wandoujia', 'db': 'spider',
	# 	'inser_table': 'item_app_wandoujia',
	# 	'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, down_num, size, version, pictures, description, category, tags, update_time, good_comm_rate, comm_num, also_likes)'},
	#
	# # spider.xiaomi
	# {'sel_columns': 'a_kaifa, a_logo, a_bao, a_name, a_size, a_ban, a_jietu, a_desc, a_fen, a_update, a_ping, a_all',
	#  'sel_table': 'xiaomi', 'db': 'spider',
	#  'inser_table': 'item_app_xiaomi',
	#  'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, size, version, pictures, description, category, update_time, comm_num, also_likes)'},
	#
	# # spider.360app
	# {
	# 	'sel_columns': 'auth, pic, pac_name, soft_name, is_official, down_num, score, apk_size, version, overview, des, app_cat, tag, update_time, comm_num, best_num, good_num, bad_num, likes',
	# 	'sel_table': '360app', 'db': 'spider',
	# 	'inser_table': 'item_app_360app',
	# 	'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, is_gov, down_num, score, size, version, pictures, description, category, tags, update_time, comm_num, good_comm_num, mid_comm_num, bad_comm_num, also_likes)'},
	#
	# # spider.hw_app
	# {
	# 	'sel_columns': 'auth, logo_url, pname, soft_name, down_num, soft_score, soft_size, version, pic_url, des, create_date, comm_num',
	# 	'sel_table': 'hw_app', 'db': 'spider',
	# 	'inser_table': 'item_app_huawei',
	# 	'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, down_num, score, size, version, pictures, description, update_time, comm_num)'},
	#
	# # spider.yingyb
	# {
	# 	'sel_columns': 'authorName, iconUrl, pkgName, appName, isOfficial, appDownCount, averageRating, fileSize, versionName, images, description, categoryName, apkPublishTime, ratingCount, sameList',
	# 	'sel_table': 'yingyb', 'db': 'spider',
	# 	'inser_table': 'item_app_yingyongbao',
	# 	'inser_columns': '(comp_full_name, app_pic, app_pack_name, app_name, is_gov, down_num, score, size, version, pictures, description, category, update_time, comm_num, same_develop)'},
	#
	# # 微信
	# # spider.yingyb 已有数据 源表字段已填充
	# # {'sel_columns': 'comp,pub_name,pic_url,weixin,feature,url_dt,crawlTime',
	# # 'sel_table': 'weixin_base_info', 'db': 'spider',
	# # 'inser_table': 'item_public_weixin',
	# # 'inser_columns': '(comp_full_name,public_name,logo,weixin_num,feature,url_detail,crawlTime)'},
	#
	# # 36氪和it橘子
	# # spider.36ke_new
	# {'sel_columns': 'company,name,web_url,logo,tag,intro,similar',
	#  'sel_table': '36ke_new', 'db': 'spider',
	#  'inser_table': 'item_product_36ke',
	#  'inser_columns': '(company_full_name,sName,web_url,company_logo,company_tags,intro,similar)'},

	# dw_online.it_company_pc 已有数据 源表字段已填充
	# {'sel_columns': 'company_full_name,sName,web_url,juzi_score,company_slogan,company_industry,sub_industry,company_address,company_logo,company_tags,product_logos,company_introduction,found_time,company_scale,company_status,mongo_id,source_url',
	# 'sel_table': 'it_company_pc', 'db': 'dw_online',
	# 'inser_table': 'item_product_it',
	# 'inser_columns': '(company_full_name,sName,web_url,juzi_score,company_slogan,company_industry,sub_industry,company_address,company_logo,company_tags,product_logos,company_introduction,found_time,company_scale,company_status,mongo_id,source_url)'},

	######++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++######################

	# baseInfo
	# 统一信用代码、企业类型、法人、注册资本、成立时间、登记机关、营业年限、登记状态、核准日期、经营范围、组织形式

	# spider.tyc_jichu_chuisou
	# {'sel_columns': 'quan_cheng, tongyi_xinyong, qiye_leixing, fa_ren, zhuce_ziben, zhuce_shijian, dengji_jiguan, yingye_nianxian, jingying_zhuangtai, hezhun_riqi, jingying_fanwei',
	# 'sel_table': 'tyc_jichu_chuisou', 'db': 'spider',
	# 'inser_table': 'comp_base_tyc',
	# 'inser_columns': '(comp_full_name, CreditCode, EconKind, LegalPerson, RegistCapi, CreateTime, BelongOrg, BusinessLife, RegistStatus, CheckDate, BusinessScope)'},

	# # tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, tongyi_xinyong, qiye_leixing, fa_ren, zhuce_ziben, zhuce_shijian, dengji_jiguan, yingye_nianxian, jingying_zhuangtai, hezhun_riqi, jingying_fanwei',
	# 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	# 'inser_table': 'comp_base_tyc',
	# 'inser_columns': '(comp_full_name, CreditCode, EconKind, LegalPerson, RegistCapi, CreateTime, BelongOrg, BusinessLife, RegistStatus, CheckDate, BusinessScope)'},

	# tyc.tyc_jichu_quan1
	# {'sel_columns': 'quan_cheng, tongyi_xinyong, qiye_leixing, fa_ren, zhuce_ziben, zhuce_shijian, dengji_jiguan, yingye_nianxian, jingying_zhuangtai, hezhun_riqi, jingying_fanwei',
	# 'sel_table': 'tyc_jichu_quan1', 'db': 'tyc',
	# 'inser_table': 'comp_base_tyc',
	# 'inser_columns': '(comp_full_name, CreditCode, EconKind, LegalPerson, RegistCapi, CreateTime, BelongOrg, BusinessLife, RegistStatus, CheckDate, BusinessScope)'},

	# spider.qichacha_search
	# {'sel_columns': 'Name, CreditCode, EconKind, OperName, RegistCapi, StartDate, BelongOrg, Status, Scope',
	# 'sel_table': 'qichacha_search', 'db': 'spider',
	# 'inser_table': 'comp_base_qcc',
	# 'inser_columns': '(comp_full_name, CreditCode, EconKind, LegalPerson, RegistCapi, CreateTime, BelongOrg, RegistStatus, BusinessScope)'},

	# spider.cyb_company
	# 企业类型、法人、注册资本、成立时间、登记状态
	# {'sel_columns': 'full_name, type, per, zcziben, found_time, statu',
	# 'sel_table': 'cyb_company', 'db': 'spider',
	# 'inser_table': 'comp_base_cyb',
	# 'inser_columns': '(comp_full_name, EconKind, LegalPerson, RegistCapi, CreateTime, RegistStatus)'},

	# spider.si_company
	# 企业类型、法人、注册资本、成立时间
	# {'sel_columns': 'quan_cheng, g_type, fa_ren, zhuce_ziben, chengli_time',
	# 'sel_table': 'si_company', 'db': 'spider',
	# 'inser_table': 'comp_base_smt',
	# 'inser_columns': '(comp_full_name, EconKind, LegalPerson, RegistCapi, CreateTime)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# website

	# spider.36ke
	# {'sel_columns': 'company, web_url', 'sel_table': '36ke', 'db': 'spider',
	#  'inser_table': 'comp_web_36ke', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.36ke_new_copy
	# {'sel_columns': 'company, web_url', 'sel_table': '36ke_new_copy', 'db': 'spider',
	#  'inser_table': 'comp_web_36ke', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.cyb_company
	# {'sel_columns': 'full_name, web', 'sel_table': 'cyb_company', 'db': 'spider',
	#  'inser_table': 'comp_web_cyb', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.it_leida_company
	# {'sel_columns': 'c_name, web', 'sel_table': 'it_leida_company', 'db': 'spider',
	#  'inser_table': 'comp_web_itLeida', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.lg_all
	# {'sel_columns': 'lg_comp_name, comp_url', 'sel_table': 'lg_all', 'db': 'spider',
	#  'inser_table': 'comp_web_lg', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.qichacha_search
	# {'sel_columns': 'Name, WebSite', 'sel_table': 'qichacha_search', 'db': 'spider',
	#  'inser_table': 'comp_web_qcc', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.tyc_jichu_chuisou
	# {'sel_columns': 'quan_cheng, w_eb', 'sel_table': 'tyc_jichu_chuisou', 'db': 'spider',
	#  'inser_table': 'comp_web_tyc', 'inser_columns': '(comp_full_name, web_url)'},

	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, w_eb', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_web_tyc', 'inser_columns': '(comp_full_name, web_url)'},

	# tyc.tyc_jichu_quan1
	# {'sel_columns': 'quan_cheng, w_eb', 'sel_table': 'tyc_jichu_quan1', 'db': 'tyc',
	#  'inser_table': 'comp_web_tyc', 'inser_columns': '(comp_full_name, web_url)'},

	# spider.xiniu_com
	# {'sel_columns': 'com_fullName, com_website', 'sel_table': 'xiniu_com', 'db': 'spider',
	#  'inser_table': 'comp_web_xiniu', 'inser_columns': '(comp_full_name, web_url)'},

	# # spider.zy_all
	# {'sel_columns': 'com_name, com_url', 'sel_table': 'zy_all', 'db': 'spider',
	#  'inser_table': 'comp_web_zy', 'inser_columns': '(comp_full_name, web_url)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# intro

	# spider.lg_all
	# {'sel_columns': 'lg_comp_name, lg_comp_intro', 'sel_table': 'lg_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_lagou', 'inser_columns': '(comp_full_name, intro)'},

	# spider.bd_intro_bj_handled
	# {'sel_columns': 'quan_cheng, dict', 'sel_table': 'bd_intro_bj_handled', 'db': 'spider',
	#  'inser_table': 'comp_intro_baidukuaizhao', 'inser_columns': '(comp_full_name, intro)'},

	# spider.bdbaike_bj
	# {'sel_columns': 'quan_cheng, intro', 'sel_table': 'bdbaike_bj', 'db': 'spider',
	#  'inser_table': 'comp_intro_baidubaike', 'inser_columns': '(comp_full_name, intro)'},

	# todoing
	# spider.cyb_company
	# 好像有问题
	# {'sel_columns': 'full_name, dec', 'sel_table': 'cyb_company', 'db': 'spider',
	#  'inser_table': 'comp_intro_cyb', 'inser_columns': '(comp_full_name, intro)'},

	# spider.si_company
	# {'sel_columns': 'quan_cheng, de_sc', 'sel_table': 'si_company', 'db': 'spider',
	#  'inser_table': 'comp_intro_smt', 'inser_columns': '(comp_full_name, intro)'},

	# spider.xiniu_com
	# {'sel_columns': 'com_fullName, com_description', 'sel_table': 'xiniu_com', 'db': 'spider',
	#  'inser_table': 'comp_intro_xiniu', 'inser_columns': '(comp_full_name, intro)'},

	# spider.zy_all
	# {'sel_columns': 'com_name, intro', 'sel_table': 'zy_all', 'db': 'spider',
	#  'inser_table': 'comp_intro_zy', 'inser_columns': '(comp_full_name, intro)'},

	# todoing 增量
	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, c_desc', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_intro_tyc', 'inser_columns': '(comp_full_name, intro)'},

	# dw_online.it_company_pc
	# {'sel_columns': 'company_full_name, company_introduction', 'sel_table': 'it_company_pc', 'db': 'dw_online',
	#  'inser_table': 'comp_intro_it', 'inser_columns': '(comp_full_name, intro)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	# logo

	# spider.tyc_jichu_chuisou
	# {'sel_columns': 'quan_cheng, logo', 'sel_table': 'tyc_jichu_chuisou', 'db': 'spider',
	#  'inser_table': 'comp_logo_tyc', 'inser_columns': '(comp_full_name, logo_url)'},

	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, logo', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_logo_tyc', 'inser_columns': '(comp_full_name, logo_url)'},

	# tyc.tyc_jichu_quan1
	# {'sel_columns': 'quan_cheng, logo', 'sel_table': 'tyc_jichu_quan1', 'db': 'tyc',
	#  'inser_table': 'comp_logo_tyc', 'inser_columns': '(comp_full_name, logo_url)'},

	# spider.qichacha_search
	# {'sel_columns': 'Name, ImageUrl', 'sel_table': 'qichacha_search', 'db': 'spider',
	#  'inser_table': 'comp_logo_qcc', 'inser_columns': '(comp_full_name, logo_url)'},

	# spider.linshi_tyc
	# {'sel_columns': 'c_name, c_logo', 'sel_table': 'linshi_tyc', 'db': 'spider',
	#  'inser_table': 'comp_logo_qcc', 'inser_columns': '(comp_full_name, logo_url)'},

	# spider.cyb_company
	# {'sel_columns': 'full_name, logo', 'sel_table': 'cyb_company', 'db': 'spider',
	#  'inser_table': 'comp_logo_cyb', 'inser_columns': '(comp_full_name, logo_url)'},

	# spider.it_leida_company
	# {'sel_columns': 'c_name, logo', 'sel_table': 'it_leida_company', 'db': 'spider',
	#  'inser_table': 'comp_logo_itLeida', 'inser_columns': '(comp_full_name, logo_url)'},

	# spider.xiniu_com
	# {'sel_columns': 'com_fullName, com_logo', 'sel_table': 'xiniu_com', 'db': 'spider',
	#  'inser_table': 'comp_logo_xiniu', 'inser_columns': '(comp_full_name, logo_url)'},

	# dw_online.it_company_pc
	# {'sel_columns': 'company_full_name, company_logo', 'sel_table': 'it_company_pc', 'db': 'dw_online',
	#  'inser_table': 'comp_logo_it', 'inser_columns': '(comp_full_name, logo_url)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# registaddr

	# spider.tyc_jichu_chuisou
	# {'sel_columns': 'quan_cheng, zhuce_dizhi', 'sel_table': 'tyc_jichu_chuisou', 'db': 'spider',
	#  'inser_table': 'comp_registaddr_tyc', 'inser_columns': '(comp_full_name, regaddr)'},

	# # tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, zhuce_dizhi', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_registaddr_tyc', 'inser_columns': '(comp_full_name, regaddr)'},

	# # tyc.tyc_jichu_quan1
	# {'sel_columns': 'quan_cheng, zhuce_dizhi', 'sel_table': 'tyc_jichu_quan1', 'db': 'tyc',
	#  'inser_table': 'comp_registaddr_tyc', 'inser_columns': '(comp_full_name, regaddr)'},
	#
	# # spider.cyb_company
	# {'sel_columns': 'full_name, address', 'sel_table': 'cyb_company', 'db': 'spider',
	#  'inser_table': 'comp_registaddr_cyb', 'inser_columns': '(comp_full_name, regaddr)'},
	#
	# # spider.si_company
	# {'sel_columns': 'quan_cheng, zhuce_didian', 'sel_table': 'si_company', 'db': 'spider',
	#  'inser_table': 'comp_registaddr_smt', 'inser_columns': '(comp_full_name, regaddr)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# officeaddr
	# spider.tyc_jichu_chuisou
	# {'sel_columns': 'quan_cheng, a_ddress', 'sel_table': 'tyc_jichu_chuisou', 'db': 'spider',
	#  'inser_table': 'comp_officeaddr_tyc', 'inser_columns': '(comp_full_name, offaddr)'},

	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, a_ddress', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_officeaddr_tyc', 'inser_columns': '(comp_full_name, offaddr)'},

	# tyc.tyc_jichu_quan1
	# {'sel_columns': 'quan_cheng, a_ddress', 'sel_table': 'tyc_jichu_quan1', 'db': 'tyc',
	#  'inser_table': 'comp_officeaddr_tyc', 'inser_columns': '(comp_full_name, offaddr)'},

	# spider.zy_all
	# {'sel_columns': 'com_name, location', 'sel_table': 'zy_all', 'db': 'spider',
	#  'inser_table': 'comp_officeaddr_zy', 'inser_columns': '(comp_full_name, offaddr)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# shortname

	# spider.lg_all
	# {'sel_columns': 'lg_comp_name, lg_short_name', 'sel_table': 'lg_all', 'db': 'spider',
	#  'inser_table': 'comp_shortname_lg', 'inser_columns': '(comp_full_name, chinese_short)'},

	# spider.it_leida_company
	# {'sel_columns': 'c_name, c_shortname', 'sel_table': 'it_leida_company', 'db': 'spider',
	#  'inser_table': 'comp_shortname_itleida', 'inser_columns': '(comp_full_name, chinese_short)'},

	# # spider.zy_all
	# {'sel_columns': 'com_name, short_name', 'sel_table': 'zy_all', 'db': 'spider',
	#  'inser_table': 'comp_shortname_zy', 'inser_columns': '(comp_full_name, chinese_short)'},
	#
	# # spider.si_company
	# {'sel_columns': 'quan_cheng, ying_jian, zhong_jian', 'sel_table': 'si_company', 'db': 'spider',
	#  'inser_table': 'comp_shortname_smt', 'inser_columns': '(comp_full_name, english_short, chinese_short)'},
	#
	# # spider.cyb_company
	# {'sel_columns': 'full_name, name', 'sel_table': 'cyb_company', 'db': 'spider',
	#  'inser_table': 'comp_shortname_cyb', 'inser_columns': '(comp_full_name, chinese_short)'},
	#
	# # dw_online.it_company_pc
	# {'sel_columns': 'company_full_name, sName', 'sel_table': 'it_company_pc', 'db': 'dw_online',
	#  'inser_table': 'comp_shortname_it', 'inser_columns': '(comp_full_name, chinese_short)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# # contactinfo
	# 电话、邮箱、传真、联系人
	# # spider.tyc_jichu_chuisou
	# {'sel_columns': 'quan_cheng, p_hone, e_mail', 'sel_table': 'tyc_jichu_chuisou', 'db': 'spider',
	#  'inser_table': 'comp_contactinfo_tyc', 'inser_columns': '(comp_full_name, phone, email)'},

	# tyc.tyc_jichu_quan
	# {'sel_columns': 'quan_cheng, p_hone, e_mail', 'sel_table': 'tyc_jichu_quan', 'db': 'tyc',
	#  'inser_table': 'comp_contactinfo_tyc', 'inser_columns': '(comp_full_name, phone, email)'},

	# tyc.tyc_jichu_quan1
	# {'sel_columns': 'quan_cheng, p_hone, e_mail', 'sel_table': 'tyc_jichu_quan1', 'db': 'tyc',
	#  'inser_table': 'comp_contactinfo_tyc', 'inser_columns': '(comp_full_name, phone, email)'},

	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	# # teaminfo
	# # tyc.tyc_main
	# 姓名、职位、简介、在职状态、头像、电话、邮箱
	# {'sel_columns': 'company, web_url', 'sel_table': '36ke', 'db': 'tyc',
	#  'inser_table': 'comp_web_36ke', 'inser_columns': '(comp_full_name, web_url)'},

]

##########################################################################################
"""
创建纬度表，需要输入 表名、表名描述，字段名、字段类型及长度、是否默认为null、字段描述
"""
create_table_list = [
	# {'table': {'name': 'comp_web_36ke', 'comment': '36氪公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# {'table': {'name': 'comp_web_cyb', 'comment': '创业邦公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# {'table': {'name': 'comp_web_itLeida', 'comment': 'it橘子雷达公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# {'table': {'name': 'comp_web_lg', 'comment': '拉钩公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# {'table': {'name': 'comp_web_qcc', 'comment': '企查查公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# {'table': {'name': 'comp_web_xiniu', 'comment': '烯牛公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# {'table': {'name': 'comp_web_zy', 'comment': '职友集公司官网'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'web_url', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '官网'}
	#  ]},
	#
	# # baseInfo
	# # 统一信用代码、企业类型、法人、注册资本、成立时间、登记机关、营业年限、登记状态、核准日期、经营范围、组织形式
	# {'table': {'name': 'comp_base_tyc', 'comment': '天眼查公司基本信息'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'CreditCode', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '统一信用代码'},
	# 	 {'name': 'EconKind', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '企业类型'},
	# 	 {'name': 'LegalPerson', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '法人'},
	# 	 {'name': 'RegistCapi', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '注册资本'},
	# 	 {'name': 'CreateTime', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '成立时间'},
	# 	 {'name': 'BelongOrg', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '登记机关'},
	# 	 {'name': 'BusinessLife', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '营业年限'},
	# 	 {'name': 'RegistStatus', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '登记状态'},
	# 	 {'name': 'CheckDate', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '核准日期'},
	# 	 {'name': 'BusinessScope', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '经营范围'},
	# 	 {'name': 'OrgType', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '组织形式'},
	#  ]},
	# # contactInfo
	# # 电话、邮箱、传真、联系人
	# {'table': {'name': 'comp_contactInfo_tyc', 'comment': '天眼查公司联系方式'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'phone', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '电话'},
	# 	 {'name': 'email', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '邮箱'},
	# 	 {'name': 'fax', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '传真'},
	# 	 {'name': 'linkman', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '联系人'},
	#  ]},
	# # teamInfo
	# # 姓名、职位、简介、在职状态、头像、电话、邮箱
	# {'table': {'name': 'comp_teamInfo_tyc', 'comment': '天眼查公司团队信息'},
	#  'colum_list': [
	# 	 {'name': 'comp_full_name', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '公司全称'},
	# 	 {'name': 'staffName', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '姓名'},
	# 	 {'name': 'staffPosition', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '职位'},
	# 	 {'name': 'staffIntro', 'type_size': 'text', 'default': 'default', 'comment': '简介'},
	# 	 {'name': 'onPositionStatus', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '在职状态'},
	# 	 {'name': 'headPic', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '头像'},
	# 	 {'name': 'staffPhone', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '电话'},
	# 	 {'name': 'staffEmail', 'type_size': 'varchar(255)', 'default': 'default', 'comment': '邮箱'},
	#  ]},

]
##########################################################################################
