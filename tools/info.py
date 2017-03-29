# -*-coding:utf-8-*-
#
# 本代码文件用于创建返回值对象
#


class Info:

    def __init__(self, infostatus, infomsg=None, inforesult=None):
        self.infostatus = infostatus
        self.infomsg = infomsg
        self.inforesult = inforesult

    def tojson(self):
        return {
            "infostatus": self.infostatus,
            "infomsg": self.infomsg,
            "inforesult": self.inforesult
        }
