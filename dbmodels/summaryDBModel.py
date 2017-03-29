# -*-coding:utf-8-*-
#
# 本代码文件用于创建数据库表格
#

from appbase import global_db as _


class Summary(_.Model):
    __tablename__ = 'summary'
    summary_id = _.Column(_.Integer, primary_key=True)
    summary_month = _.Column(_.String(10))
    summary_out = _.Column(_.Numeric(15, 3))
    summary_in = _.Column(_.Numeric(15, 3))
    summary_lent = _.Column(_.Numeric(15, 3))
    summary_borrow = _.Column(_.Numeric(15, 3))
    summary_user = _.Column(_.Integer, _.ForeignKey("user.user_id"))

    def __init__(self, summary_month, summary_out, summary_in, summary_lent, summary_borrow, summary_user):
        self.summary_month = summary_month
        self.summary_out = summary_out
        self.summary_in = summary_in
        self.summary_lent = summary_lent
        self.summary_borrow = summary_borrow
        self.summary_user = summary_user

    def tolist(self):
        return [self.summary_id, self.summary_month, self.summary_out, self.summary_in,
                self.summary_lent, self.summary_borrow, self.summary_user]