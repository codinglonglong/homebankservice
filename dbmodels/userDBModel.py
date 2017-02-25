# -*-coding:utf-8-*-
#
# 本代码文件用于创建数据库表格
#

from appbase import global_db as _


class User(_.Model):
    __tablename__ = 'user'
    user_id = _.Column(_.Integer, primary_key=True)
    user_email = _.Column(_.String(30), unique=True)
    user_password = _.Column(_.String(30), nullable=False)
    user_token = _.Column(_.String(512))
    user_timestamp = _.Column(_.String(20))
    user_verification = _.Column(_.String(6))

    def __init__(self, user_email, user_password, user_token=None, user_timestamp=None, user_verification=None):
        self.user_email = user_email
        self.user_password = user_password
        self.user_token = user_token
        self.user_timestamp = user_timestamp
        self.user_verification = user_verification

    def tolist(self):
        return [self.user_id, self.user_email, self.user_password, self.user_token,
                self.user_timestamp, self.user_verification]