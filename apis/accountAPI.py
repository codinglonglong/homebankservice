# -*-coding:utf-8-*-
#
# 本代码文件用于创建服务接口
#

from appbase import global_api as api
from apimodels.accountAPIModel import accountmodel
from daos.accountDAO import AccountDAO
from flask_restplus import Resource

ns_account = api.namespace("account", description="账目管理")


@ns_account.route("/<string:user_token>/<int:account_id>")
@ns_account.param("user_token", "用户标识")
@ns_account.param("account_id", "账目编号")
class AccountItem(Resource):

    def get(self, user_token, account_id):
        """
        Delete An Account
        """
        return AccountDAO.removeaccount(user_token, account_id)


@ns_account.route("/<string:user_token>")
@ns_account.param("user_token", "用户标识")
class Account(Resource):

    @ns_account.expect(accountmodel)
    def post(self, user_token):
        """
        Add Account
        """
        return AccountDAO.addaccount(user_token, api.payload)


@ns_account.route("/<int:page>/<string:user_token>")
@ns_account.param("page", "页码")
@ns_account.param("user_token", "用户标识")
class AccountPage(Resource):

    def get(self, page, user_token):
        """
        Get Account By Date Length
        """
        return AccountDAO.getaccountbydatelength(user_token, page)


@ns_account.route("/borrow/<string:user_token>")
@ns_account.param("user_token", "用户标识")
class Borrow(Resource):

    def get(self, user_token):
        """
        Get Account About Borrow And Lent
        """
        return AccountDAO.getborrowaccount(user_token)


@ns_account.route("/summary/<string:user_token>")
@ns_account.param("user_token", "用户标识")
class Summary(Resource):

    def get(self, user_token):
        """
        Get Summary Of Account
        """
        return AccountDAO.getsummaryaccount(user_token)
