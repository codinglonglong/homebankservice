# -*-coding:utf-8-*-
#
# 本代码文件用于创建用户标记
#

import uuid
import hashlib
import time
from appbase import global_db as db
from dbmodels.userDBModel import User


class Token:

    def __init__(self):
        pass

    @staticmethod
    def gettoken():
        uuidstr = str(uuid.uuid1())
        timestr = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        tokenbody = uuidstr + timestr
        token = hashlib.md5(tokenbody).hexdigest()
        return token

    @staticmethod
    def getidbytoken(token):
        flag = db.session.query(User.user_id).filter(User.user_token == token).first()
        if flag:
            return flag[0]
        return None
