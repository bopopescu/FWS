# -*- coding: utf-8 -*-

from __init__ import db
from datetime import datetime


class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(64),unique = True)
	#第一个参数：关系的另一端是哪个模型
	#第二个参数：backref向User模型中添加一个role属性
	users = db.relationship('User',backref = 'role')

	def __repr__(self):
		return self.name


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(64),unique = True,index = True)
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
	posts = db.relationship('Post',backref = 'author',lazy = 'dynamic')

	def __repr__(self):
		return self.username
		

#文章模型
class Post(db.Model):
	"""文章模型"""
	__tablename__ = 'posts'
	id = db.Column(db.Integer,primary_key = True)
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index = True,default = datetime.utcnow())
	author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
	def __repr__(self):
		return self



