import logging
import pymysql
import jieba
import xml.etree.ElementTree as ET
import traceback
import requests
from scrapy import Selector


def get_dict():
	"""
		加载地区配置文件，放入到 chain_tree 中
	:return:
	"""
	tree = ET.ElementTree(file='area.xml')
	root = tree.getroot()
	for p in root:
		print(p)


def req():
	with open('area.xml', 'r') as f:
		xml = f.read()
	sel = Selector(text=xml)
	address = sel.xpath('//address')
	all = []
	province_tags = address.xpath('./province')
	for province_tag in province_tags:
		province = province_tag.xpath('./@name').extract_first()
		all.append(province)
		city_tags = province_tag.xpath('./city')
		for city_tag in city_tags:
			city = city_tag.xpath('./@name').extract_first()
			all.append(city)
			country_tags = city_tag.xpath('./country')
			for country_tag in country_tags:
				country = country_tag.xpath('./@name').extract_first()
				country_handle = city + country
				all.append(country_handle)
	return all


if __name__ == '__main__':
	all = req()
	print(len(all))
