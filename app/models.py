#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2018/4/12  9:09
# IDE:         PyCharm
# anthor:      ZT@gufan

from app.extensions import db


#定义多对多关系 注意定义一个中间表
posts_tags=db.Table("posts_tags",
                    db.Column('post_id',db.Integer,db.ForeignKey("posts.id")),
                    db.Column('tag_id',db.Integer,db.ForeignKey('tags.id')))


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
    comments=db.relationship('Comment',backref="posts",lazy="dynamic")
    tags=db.relationship('Tag',secondary=posts_tags,
                         backref=db.backref('posts',lazy='dynamic'))
    def __repr__(self):
        return "<Model Post {}>".format(self.title)

#
class Comment(db.Model):
    __tablename__="comments"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    text=db.Column(db.Text())
    date=db.Column(db.DateTime())
    post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))

    def __repr__(self):
        return "<Model Comment {}>".format(self.name)

class Tag(db.Model):
    __tablename__="tags"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))

    def __repr__(self):
        return "<Model Tag {} >".format(self.name)