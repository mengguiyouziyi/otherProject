import pymysql
import os
import time
import logging
import redis

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_redis_db(host, port=6379, db=0):
	"""
	获取redis实例连接
	:param host:
	:param port:
	:param db:
	:return:
	"""
	pool = redis.ConnectionPool(host=host, port=port, db=db)
	redis_db = redis.StrictRedis(connection_pool=pool, decode_responses=True)
	return redis_db


def get_redis_field(redis_db, key):
	"""
	获取redis key中的所有field
	:param redis_db:
	:param key:
	:return:
	"""
	return redis_db.hkeys(key)


def get_redis_allhash(redis_db, key):
	"""
	获取redis key中的所有field,value
	:param redis_db:
	:param key:
	:return:
	"""
	return redis_db.hgetall(key)


def in_redis_hash(redis_db, key, field, value):
	"""
	向redis中插入hash数据
	:param redis_db:
	:param key:
	:param value:
	:param field:
	:return:
	"""
	redis_db.hmset(key, {field: value})


def get_redis_hash(redis_db, key, field):
	"""
	返回redis中的hash值
	:param redis_db:
	:param key:
	:param field:
	:return:
	"""
	return redis_db.hget(key, field)


def in_redis_string(redis_db, key, value):
	"""
	向redis中插入string数据
	:param redis_db:
	:param key:
	:param value:
	:return:
	"""
	redis_db.set(key, value)


def get_redis_string(redis_db, key):
	"""
	返回redis中的string值
	:param redis_db:
	:param key:
	:return:
	"""
	return redis_db.get(key)


