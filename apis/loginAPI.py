# -*-coding:utf-8-*-
#
# 本代码文件用于创建服务接口
#

from appbase import global_api as api
from apimodels.loginAPIModel import loginmodel
from apimodels.loginAPIModel import passwordmodel
from daos.loginDAO import LoginDAO
from flask_restplus import Resource

ns_login = api.namespace("login", description="用户管理")


@ns_login.route("/")
class Login(Resource):

    @ns_login.expect(loginmodel)
    def post(self):
        """
        User Login
        """
        return LoginDAO.login(api.payload)


@ns_login.route("/<string:user_token>")
@ns_login.param("user_token", "用户标识")
class Logout(Resource):

    def get(self, user_token):
        """
        User Logout
        """
        return LoginDAO.logout(user_token)

    @ns_login.expect(passwordmodel)
    def put(self, user_token):
        """
        User Change Password
        """
        return LoginDAO.changepassword(user_token, api.payload)
