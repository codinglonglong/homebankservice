# -*-coding:utf-8-*-
#
# 本代码文件用于创建自定义装饰器
#

from appbase import global_db as db
from dbmodels.userDBModel import User
from flask import jsonify
from tools.info import Info


def checktoken(func):
    def _(user_token="", *args, **kwargs):
        if db.session.query(User).filter(User.user_token == user_token).count() > 0:
            if args and kwargs:
                return func(user_token, args, kwargs)
            elif args:
                return func(user_token, args)
            elif kwargs:
                return func(user_token, kwargs)
            else:
                return func(user_token)
        else:
            return jsonify(Info(False, "用户未登录").tojson())
    return _
