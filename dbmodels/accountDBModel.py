# -*-coding:utf-8-*-
#
# 本代码文件用于创建数据库表格
#

from appbase import global_db as _


class Account(_.Model):
    __tablename__ = 'account'
    account_id = _.Column(_.Integer, primary_key=True)
    account_item = _.Column(_.String(30), nullable=False)
    account_money = _.Column(_.Numeric(15, 3), nullable=False)
    account_type = _.Column(_.Integer, _.ForeignKey("type.type_id"), nullable=False)
    account_date = _.Column(_.String(10), nullable=False)
    account_addition = _.Column(_.String(200))
    account_user = _.Column(_.Integer, _.ForeignKey("user.user_id"), nullable=False)

    def __init__(self, account_item, account_money, account_type, account_date, account_addition, account_user):
        self.account_item = account_item
        self.account_money = account_money
        self.account_type = account_type
        self.account_date = account_date
        self.account_addition = account_addition
        self.account_user = account_user

    def tolist(self):
        return [self.account_id, self.account_item, self.account_money,
                self.account_type, self.account_date, self.account_addition, self.account_user]
