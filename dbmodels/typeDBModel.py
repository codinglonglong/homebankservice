# -*-coding:utf-8-*-
#
# 本代码文件用于创建数据库表格
#

from appbase import global_db as _


class AccountType(_.Model):
    __tablename__ = 'type'
    type_id = _.Column(_.Integer, primary_key=True)
    type_text = _.Column(_.String(5), nullable=False)

    def __init__(self, type_text):
        self.type_text = type_text

    def tolist(self):
        return [self.type_id, self.type_text]