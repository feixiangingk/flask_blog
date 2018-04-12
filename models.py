#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2018/4/12  9:09
# IDE:         PyCharm
# anthor:      ZT@gufan

from ext import db


class User(db.Model):

    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),nullable=False)
    password=db.Column(db.String(255),nullable=False)
    posts=db.relationship('Post',backref="users",lazy="dynamic")

    def __repr__(self):
        return "<Model User {}>".format(self.username)

class Post(db.Model):
    __tablename__="posts"
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(255))
    text=db.Column(db.Text())
    publish_date=db.Column(db.DateTime)
    #设置外键
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return "<Model Post {}>".format(self.title)