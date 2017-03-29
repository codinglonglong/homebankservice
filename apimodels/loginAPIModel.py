# -*-coding:utf-8-*-
#
# 本代码文件用于创建接口模型
#

from appbase import global_api
from flask_restplus import fields

loginmodel = global_api.model('Login', {
    'user_email': fields.String(required=True, description="email"),
    'user_password': fields.String(required=True, description="password")
})

passwordmodel = global_api.model('Password', {
    'user_oldpassword': fields.String(required=True, description="old password"),
    'user_newpassword': fields.String(required=True, description="new password")
})
