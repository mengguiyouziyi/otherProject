#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    对注册地址进行清洗的程序：
"""

import logging
import pymysql
import jieba
import xml.etree.ElementTree as ET
import traceback

# 创建一个logger
logger = logging.getLogger('RegistAddr_Log')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('RegistAddr_Process.log')
# fh.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
# ---------↑↑↑↑↑↑↑定义日志↑↑↑↑↑↑↑↑-----------

db_host = 'etl2.innotree.org'
db_user = 'etl_m'
db_password = 'innotree'
db_name = 'dimension_sum'
db_port = 3308
connection = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name,
                             port=db_port, charset='utf8', cursorclass=pymysql.cursors.SSCursor
                             )
# 来源优先循序
youxianji = {
    "tyc": 0
}

china_tree = {}
zhixiashi_list = []
# 唯一 ID
one_id = 0
# 控制插入数量
all_nums = 0
# 来源
source = ""
# 得分
score = 0
# 步长
buchang = 2000


def readAllId():
    """
        从数据库中，读取所有 ID
    """
    logger.info("从数据库中读取所有的id")
    all_id = []
    with connection.cursor() as cursor:
        for i in range(0, 10):
            logger.info("处理第 {i} 张表".format(i=i))
            cursor.execute("select count(id) from comp_registaddr_sum%s", i)
            # 获得到该表下所有ID 的总数
            _all = cursor.fetchall()
        # with connection.cursor() as cursor:
            # 阈值
            for x in range(0, _all // buchang):
                logger.info("处理 {buchang} 条".format(buchang=buchang))
                sql = """select distinct only_id from comp_registaddr_sum%s limit {start},{buchang}""".format(start=x*buchang, buchang=buchang)
                cursor.execute(sql, x)
                result = cursor.fetchall()
                for one_id in result:
                    all_id.append(one_id[0])
                processAll(all_id)


def processAll(list_id):
    """
        遍历所有 ID，对数据进行查找
    :param list_id:
    :return:
    """
    print(list_id.__len__())
    for x in list_id:
        global one_id
        one_id = x
        processOneId(x)


def processOneId(one_id):
    """
        根据指定 ID 到数据库中查找，返回结果到 insertOne
    :param one_id:
    :return:
    """
    try:
        with connection.cursor() as cursor:
            sql = """select comp_full_name,regaddr,only_id,source_y,load_time from comp_registaddr_sum%s where only_id = %s"""
            cursor.execute(sql, (int(one_id) % 10, one_id))
            result = cursor.fetchall()
            logger.info("开始处理 {id} 的记录".format(id=one_id))
            process(result)
    except:
        logger.error("处理失败 {id} 的记录".format(id=one_id))
        print(traceback.print_exc())


def process(collections):
    """
        开始对记录进行清洗
    :param collections:
    :return:
    """
    # 如果是一条记录
    if collections.__len__() == 1:
        # 取出来源
        one = collections[0]
        global source
        source = one[3]
        if "未公开" not in one[1] and "暂无" not in one[1]:
            registaddr = one[1]
            registaddr = panduan(registaddr)
            if registaddr == "没有找到" or registaddr == "不能分割":
                pass
            else:
                values = (one[0], registaddr[0], registaddr[1], registaddr[2], registaddr[3], one_id, one[3], one[4], score+descore())
                insertO(values)
    # 含有多条
    else:
        minvalue = []
        for one in collections:
            minvalue.append(youxianji.get(one[3]))
        minv = min(minvalue)
        # 获得最小来源的数据
        for one in collections:
            if minv == youxianji.get(one[3]):
                if "未公开" in one[1] or "暂无" in one[1]:
                    ne = list(collections)
                    ne.remove(one)
                    process(ne)
                else:
                    registaddr = one[1]
                    registaddr = panduan(registaddr)
                    if registaddr == "没有找到" or registaddr == "不能分割":
                        ne = list(collections)
                        ne.remove(one)
                        process(collections)
                        return
                    else:
                        values = (one[0], registaddr[0], registaddr[1], registaddr[2], registaddr[3], one_id, one[3], one[4], score + descore())
                        insertO(values)


def panduan(address):
    global score
    # 进行分词
    all_word = jieba.lcut(address)
    # 如果市重复了
    if all_word.__len__() > 2 and (all_word[1] == all_word[2]):
        all_word.remove(all_word[1])
    # 当长度大于等于3
    if all_word.__len__() >= 3:
        # 如果有地区重复，则从第一个中去除地区，进行第一步处理
        if all_word[1] in all_word[0]:
            all_word[0].replace(all_word[1], '')
        if all_word[0].endswith("省") and all_word[1].endswith("市") and (all_word[2].endswith("区") or all_word[2].endswith("县")):
            score = 5
            return address, all_word[0], all_word[1], all_word[2]
        else:
            # 提取省和直辖市，判断 第一个字段是否是省或者直辖市
            for province in china_tree.keys():
                if all_word[0] in province:
                    # 判断 第一个字段是否是省（包括直辖市）
                    for shi in china_tree.get(province).keys():
                        # 如果获得的是直辖区，则判断下一个字段是否是对应的区
                        if "辖区" in shi:
                            for qu in china_tree.get(province).get(shi):
                                if all_word[1] in qu:
                                    result = province + qu
                                    for one in all_word[2:]:
                                        result += one
                                    score = 4
                                    return result, province, shi, qu
                        # 不是辖区则进行市
                        if all_word[1] in shi:
                            for qu in china_tree.get(province).get(shi):
                                # 到这里已经确定有省市区
                                if all_word[2] in qu:
                                    result = province + shi + qu
                                    for one in all_word[2:]:
                                        result += one
                                    score = 4
                                    return result, province, shi, qu
                            # 有省有市，没有区的进行输出吗？
                            result = province + shi
                            for one in all_word[2:]:
                                result += one
                            score = 3
                            return result, province, shi, "null"
                # 如果不是省则判断是否是直辖市的区                       
                elif isTrue(all_word[0]):
                    for shi in china_tree.get(province).keys():
                        if '辖区' in shi:
                            # 获得该直辖区下面的所有区
                            for one in china_tree.get(province).values():
                                for qu in one:
                                    if all_word[0] in qu:
                                        if province != "上海市":
                                            result = province + qu
                                            for a in all_word[1:]:
                                                result += a
                                            score = 3
                                            return result, province, shi, qu
                                        else:
                                            result = qu
                                            for a in all_word[1:]:
                                                result += a
                                            score = 4
                                            return result, province, shi, qu
                # 判断不是直辖市所对应的区
                # else:
                #     for shi in china_tree.get(province).keys():
                #         if "辖区" not in shi and all_word[0] in shi:
                #             # all_word[0] = shi
                #             result = province+shi
                #             for one in all_word[1:]:
                #                 result += one
                #             return result
            for province in china_tree.keys():
                for shi in china_tree.get(province).keys():
                    if "辖区" not in shi and all_word[0] in shi:
                        result = province + shi
                        for one in all_word[1:]:
                            result += one
                        score = 4
                        return result, province, shi, "null"
        return "没有找到"
    # 分割字段小于3的
    else:
        # 判断是否是直辖市和区，在只有2个字段的时候
        return "不能分割"


def isTrue(one):
    """
        判断是否是所有直辖市的区
    :param one:
    :return:
    """
    for qu in zhixiashi_list:
        if one in qu:
            return True
    return False


def insertO(one):
    """
        插入一条数据
    :param one:
    :return:
    """
    global all_nums
    all_nums += 1
    if all_nums == 2000:
        connection.commit()
        all_nums = 0
    with connection.cursor() as cursor:
        sql = """insert into comp_registaddr_sum_result(comp_full_name,regaddr,province,city,district,only_id,source_y,load_time,score) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, one)


def descore():
    """
        判断一个记录的得分
    :param one:
    :return:
    """
    if source == "tyc":
        return 5
    elif source == "baike":
        return 4
    elif source == "baidukuaizhao":
        return 3
    else:
        return 2


def testXML():
    """
        加载地区配置文件，放入到 chain_tree 中
    :return:
    """
    logger.info("加载地区配置文件")
    tree = ET.ElementTree(file='area.xml')
    root = tree.getroot()
    global china_tree
    for child_of_root in root:
        shi_map = {}
        province = child_of_root.attrib.get('name')
        for city in child_of_root:
            shi = city.attrib.get('name')
            qulist = []
            for country in city:
                if province in ('北京市', '上海市', '重庆市', '天津市'):
                    zhixiashi_list.append(country.attrib.get('name'))
                qulist.append(country.attrib.get('name'))
            shi_map[shi] = qulist
        china_tree[province] = shi_map

if __name__ == '__main__':
    testXML()
    # result = panduan("四川省达州市通川区罗江镇农贸市场内")
    # print(result)
    readAllId()
    # processAll(all_id)
    connection.commit()
    connection.close()
