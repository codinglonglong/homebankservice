# -*-coding:utf-8-*-
#
# 本代码文件是整个程序的入口文件
#

import dbbuilder
from appbase import global_app
from tools.log import logger
import apis  # 引入有效的程序接口


dbbuilder.create_db()
logger.info("app started")
global_app.run(host="0.0.0.0", port=9001, debug=True)

