#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2018/4/11  11:41
# IDE:         PyCharm
# anthor:      ZT@gufan


from __future__ import unicode_literals
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
class Config(object):
    pass

class DevConfig(object):
    DEBUG=True
    DATABASE_USER='root'
    DATABASE_PWD="123456"
    DATABASE_HOST='127.0.0.1'
    DATABASE_PORT=3306
    DATABASE_NAME='test'
    SQLALCHEMY_DATABASE_URI='mysql://' + DATABASE_USER + ':' + DATABASE_PWD + '@' + \
                          DATABASE_HOST + ':' + str(DATABASE_PORT) + '/' + DATABASE_NAME + '?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS=True