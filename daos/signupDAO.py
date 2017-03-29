# -*-coding:utf-8-*-
#
# 本代码文件用于完成数据库操作
#

from flask import jsonify
from appbase import global_db as db
from dbmodels.userDBModel import User
from tools.info import Info
from tools.log import logger


class SignupDAO:

    def __init__(self):
        pass

    @staticmethod
    def checkuseremail(user_email):
        if User.query.filter(User.user_email == user_email).count() > 0:
            return jsonify(Info(False, "已存在的邮箱").tojson())
        else:
            return jsonify(Info(True, "可以使用的邮箱地址").tojson())

    @staticmethod
    def adduser(user):
        user_email = user["user_email"]
        user_password = user["user_password"]
        user = User(user_email, user_password)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            # print(e.args)
            # print(e.detail)
            # print(e.instance)
            # print(e.message)
            # print(e.orig)
            # print(e.params)
            # print(e.statement)
            # print(e.orig.args)
            # print(e.orig.errno)  错误代码
            # print(e.orig.message)  错误信息
            # print(e.orig.msg)
            # print(e.orig.sqlstate)
            print(e)
            logger.error(e)
            if int(e.orig.errno) == 1062:
                return jsonify(Info(False, "注册失败，已存在的邮箱").tojson())
            elif int(e.orig.errno) == 1146:
                return jsonify(Info(False, "注册失败，数据库错误").tojson())
        else:
            return jsonify(Info(True, "注册成功").tojson())
