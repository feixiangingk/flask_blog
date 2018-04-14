#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/14 13:59
# software:     PyCharm
# from models import db,User,Post,Comment

def views_app(app):

    @app.route('/')
    def hello_world():
        return 'Hello World!'
