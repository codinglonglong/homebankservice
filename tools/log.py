# -*-coding:utf-8-*-
#
# 本代码文件用于记录日志
#

import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time

logger = logging.getLogger()
if len(logger.handlers) == 0:
    level = logging.INFO
    starttime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    if not os.path.exists("logs/"+starttime+".txt"):
        os.mknod("logs/"+starttime+".txt")
    filename = "logs/"+starttime+".txt"
    formatstr = '%(asctime)s\t%(levelname)s\t%(module)s\t%(funcName)s\tLine:%(lineno)d\t%(message)s'
    hdlr = TimedRotatingFileHandler(filename, "midnight", 1, 10)
    fmt = logging.Formatter(formatstr)
    hdlr.setFormatter(fmt)
    logger.addHandler(hdlr)
    logger.setLevel(level)
