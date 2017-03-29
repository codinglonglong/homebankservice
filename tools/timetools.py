# -*-coding:utf-8-*-
#
# 本代码文件用于完成日期时间方面的计算
#


def datestrtomonth(datestr):
    """
    将日期字符串转换为月份
    """
    year, month, _ = datestr.split("-")
    return str(year) + "-" + str(month)
