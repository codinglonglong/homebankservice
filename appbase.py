# -*-coding:utf-8-*-
#
# 本代码文件用于创建重要的全局对象
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from conf import dbconnection
from flask_restplus import Api
from flask_cors import CORS, cross_origin


global_app = Flask(__name__)

CORS(global_app)

global_app.config['SQLALCHEMY_DATABASE_URI'] = dbconnection

global_db = SQLAlchemy(global_app)

global_api = Api(global_app, version="1.0", title="Homebank API", description="小家手帐")
