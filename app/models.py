# -*- coding: utf-8 -*-


from __init__ import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


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
	password_hash = db.Column(db.String(128))

	@property
	def password(self):
		raise AttributedError('password is not a readable attribute')

	@password.setter
	def password(self,password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)

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



