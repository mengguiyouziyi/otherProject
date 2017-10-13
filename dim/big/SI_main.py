from SI_util import main
from SI_config import sel_inser_list


for sel_inser in sel_inser_list:
	print(sel_inser['sel_table'])
	args = [sel_inser['sel_columns'], sel_inser['sel_table'], sel_inser['db'], sel_inser['inser_table'], sel_inser['inser_columns']]

	main(*args)

