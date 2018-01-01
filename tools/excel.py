# -*-coding:utf-8-*-
#
# 本代码文件用于读写Excel文件
#

from pyexcel_xls import save_data
from pyexcel_xls import get_data
from collections import OrderedDict
import os
from dbmodels.summaryDBModel import Summary
from dbmodels.accountDBModel import Account
from appbase import global_db as db


def writetofile(sheetname, datas, user_token):
    if os.path.exists("data/" + str(user_token) + "/data.xls"):
        data = get_data("data/" + str(user_token) + "/data.xls")
    else:
        os.mkdir("data/"+str(user_token))
        data = OrderedDict()
    sheet = []
    for dt in datas:
        sheet.append(dt)
    data.update(OrderedDict({sheetname: sheet}))
    save_data("data/" + str(user_token) + "/data.xls", data)


def readfromfile(fileurl, userid):
    data = get_data(fileurl)
    summarylist = data["summarylist"]
    accountlist = data["accountlist"]
    try:
        for si in summarylist:
            su = Summary(si[0], si[1], si[2], si[3], si[4], userid)
            db.session.add(su)
        for ai in accountlist:
            if len(ai) == 5:
                ac = Account(ai[0], ai[1], ai[2], ai[3], ai[4], userid)
            if len(ai) == 4:
                ac = Account(ai[0], ai[1], ai[2], ai[3], "", userid)
            db.session.add(ac)
    except Exception as e:
        return False
    else:
        return True
