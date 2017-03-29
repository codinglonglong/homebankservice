# -*-coding:utf-8-*-
#
# 本代码文件用于创建接口模型
#

from appbase import global_api
from flask_restplus import fields


accountmodel = global_api.model('Account', {
    'account_item': fields.String(required=True, description="item"),
    'account_money': fields.String(required=True, description="money"),
    'account_type': fields.Integer(required=True, description="type id"),
    'account_date': fields.Date(required=True, description="date"),
    'account_addition': fields.String(description="addition"),
    'account_user': fields.Integer(required=True, description="user id")
})