# coding:utf-8
"""
项目读取配置文件
"""
##########################################################################################
"""
搜索源数据表全部纬度，插入数据表，只需传入 
sel_table(搜索表名),
inser_table(插入表名)，inser_columns(插入字段) 即可
"""
sel_inser_list = [
	# spider.tyc_gudongxin xin 10438374  13218691
	{'sel_table': 'tyc_gudongxin', 'inser_table': 'comp_gudong_tyc',},
	 # 'inser_columns': '(comp_full_name, t_id, p_name, p_tid, chuzi_bili, renjiao_chuzi)'},
	# spider.tyc_gudongxin1
	# {'sel_table': 'tyc_gudongxin1', 'inser_table': 'm_tyc_gudongxin',
	#  'inser_columns': '(comp_full_name, t_id, p_name, p_tid, chuzi_bili, renjiao_chuzi)'},

	# spider.tyc_out_investment xin 691061
	# {'sel_table': 'tyc_out_investment', 'inser_table': 'comp_duiwai_tyc',},
	 # 'inser_columns': '(comp_full_name,t_id,invest_name,invest_tid,representative,rep_tid,register_amount,register_date,investment_amount,investment_rate,com_status)'
	# spider.tyc_out_investment1
	# {'sel_table': 'tyc_out_investment1', 'inser_table': 'm_tyc_out_investment',
	#  'inser_columns': '(comp_full_name,t_id,invest_name,invest_tid,representative,rep_tid,register_amount,register_date,investment_amount,investment_rate,com_status)'},

	# # spider_dim.jigou_contactinfo_smt ==> spider_dim.jigou_contactinfo_smt_copy
	# {'sel_table': 'jigou_contactinfo_smt', 'inser_table': 'jigou_contactinfo_smt_copy1'},
	#
	# # spider_dim.jigou_teaminfo_smt
	# {'sel_table': 'jigou_teaminfo_smt', 'inser_table': 'jigou_teaminfo_smt_copy1'},

	# spider_dim.tyc_core_team
	{'sel_table': 'tyc_core_team', 'inser_table': 'comp_teaminfo_tyc'},
]
##########################################################################################
"""
创建纬度表，需要输入 表名、表名描述，字段名、字段类型及长度、是否默认为null、字段描述
"""
create_table_list = [

]
##########################################################################################
