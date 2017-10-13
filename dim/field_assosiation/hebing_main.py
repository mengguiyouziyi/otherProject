from hebing import main
from hebing_config import sel_inser_list

for sel_inser in sel_inser_list:
	# args = [sel_inser['sel_table'], sel_inser['inser_table'], sel_inser['inser_columns']]
	main(sel_inser['sel_table'], sel_inser['inser_table'])
