# -*-coding:utf-8-*-
#
# 本代码文件用于加入测试记录
#

import redis
from conf import debughost
from conf import debugport

r = redis.StrictRedis(host=debughost, port=debugport, db=0)


def r_set(key, value):
    r.set(key, value)


def r_get(key):
    r.get(key)


