# -*-coding:utf-8-*-
#
# 本代码文件用于完成数据库操作
#

from flask import jsonify
from appbase import global_db as db
from dbmodels.userDBModel import User
from tools.info import Info
from tools.log import logger
from tools.token import Token
from tools.decorator import checktoken
from sqlalchemy import and_
from tools.cleaner import cleaner


class LoginDAO:

    def __init__(self):
        pass

    @staticmethod
    @checktoken
    def changepassword(user_token, params):
        password = params[0]
        user_oldpassword = password["user_oldpassword"]
        user_newpassword = password["user_newpassword"]
        user = User.query.filter(and_(
            User.user_id == Token.getidbytoken(user_token),
            User.user_password == user_oldpassword
        )).first()
        if not user:
            return jsonify(Info(False, "原密码错误").tojson())
        user.user_password = user_newpassword
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            logger.error(e)
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            return jsonify(Info(True, "密码修改成功").tojson())

    @staticmethod
    @checktoken
    def logout(user_token):
        try:
            user = User.query.filter(
                User.user_token == user_token).first()
            user.user_token = ""
            db.session.commit()
        except Exception as e:
            print(e)
            logger.error(e)
            return jsonify(Info(False, "数据库错误").tojson())
        else:
            cleaner()
            return jsonify(Info(True, "用户成功退出").tojson())

    @staticmethod
    def login(user):
        user_email = user["user_email"]
        user_password = user["user_password"]
        user_token = Token.gettoken()
        try:
            loginflag = User.query.filter(and_(
                User.user_email == user_email,
                User.user_password == user_password)).count()
        except Exception as e:
            print(e)
            logger.error(e)
            return jsonify(Info(False, "登陆失败，数据库错误").tojson())
        else:
            if loginflag == 0:
                return jsonify(Info(False, "登陆失败，用户名或密码错误").tojson())
            else:
                user = User.query.filter(and_(
                    User.user_email == user_email,
                    User.user_password == user_password)).first()
                user.user_token = user_token
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    logger.error(e)
                    return jsonify(Info(False, "登陆失败，数据库错误").tojson())
                else:
                    return jsonify(Info(True, "登陆成功", user_token).tojson())

