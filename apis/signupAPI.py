# -*-coding:utf-8-*-
#
# 本代码文件用于创建服务接口
#

from appbase import global_api as api
from apimodels.signupAPIModel import signupmodel
from daos.signupDAO import SignupDAO
from flask_restplus import Resource

ns_signup = api.namespace("signup", description="用户注册")


@ns_signup.route("/")
class Signup(Resource):

    @ns_signup.expect(signupmodel)
    def post(self):
        """
        User Sign Up
        """
        return SignupDAO.adduser(api.payload)


@ns_signup.route("/<string:user_email>")
class SignupCheck(Resource):

    def get(self, user_email):
        """
        Check User Email
        """
        return SignupDAO.checkuseremail(user_email)

