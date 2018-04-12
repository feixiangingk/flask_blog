#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2018/4/11  11:53
# IDE:         PyCharm
# anthor:      ZT@gufan
from __future__ import unicode_literals
from flask_script import Manager,Server
from __init__ import create_app,app
from ext import db
from models import User,Post
# app=create_app()
manager=Manager(app)

manager.add_command("server",Server('0.0.0.0',port=9000))

@manager.shell
def make_shell_context():
    '''
    创建一个载入预设配置的上下文环境，不用在Python console一步步导包了
    后期还可以将db 等传进来
    :return:
    '''
    return dict(app=create_app(),db=db,User=User,Post=Post)

if __name__ == '__main__':
    manager.run()
