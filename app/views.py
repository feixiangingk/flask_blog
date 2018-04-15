#-*-coding:utf-8-*-
# author:       lenovo
# createtime:   2018/4/14 13:59
# software:     PyCharm
# from models import db,User,Post,Comment
from flask import jsonify

def views_app(app):

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/test',methods=['POST','GET'])
    def test():
        return jsonify({'hello':'gufan'}),{'Access-Control-Allow-Origin':'127.0.0.1:8020',
                                           "Access-Control-Allow-Headers": "X-Requested-With",
                                           "Access-Control-Allow-Methods": "PUT,POST,GET,DELETE,OPTIONS"}
