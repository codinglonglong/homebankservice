# -*-coding:utf-8-*-
#
# 本代码文件用于创建数据库表格
#

from appbase import global_db as _
from dbmodels.typeDBModel import AccountType
import dbmodels  # 引入有效的数据库模型


def create_db():
    _.create_all()
    if AccountType.query.count() == 0:
        typelist = [
            "支出", "收入", "贷出", "借入"
        ]
        for tl in typelist:
            _.session.add(AccountType(tl))
        _.session.commit()
