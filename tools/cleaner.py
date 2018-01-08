# -*-coding:utf-8-*-
#
# 本代码文件用于清理临时文件
#

from daos.accountDAO import AccountDAO
from datetime import datetime
from datetime import timedelta
import os


def cleaner():
    # 清空导入导出的文件
    AccountDAO.cleantempfiles()
    # 清理日志文件
    tdel = timedelta(days=5)
    lasttime = (datetime.now() - tdel).strftime("%Y%m%d")
    loglist = os.listdir("logs")
    loglist = [x for x in loglist if x[:8] < lasttime]
    for ll in loglist:
        os.remove("logs/" + ll)