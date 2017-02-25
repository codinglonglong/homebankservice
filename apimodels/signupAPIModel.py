# -*-coding:utf-8-*-
#
# 本代码文件用于创建接口模型
#

from appbase import global_api
from flask_restplus import fields

signupmodel = global_api.model('Signup', {
    'user_email': fields.String(required=True, description="email"),
    'user_password': fields.String(required=True, description="password")
})