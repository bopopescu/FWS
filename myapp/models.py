# -*- coding: utf-8 -*-


from __init__ import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin
from __init__ import login_manager


#加载用户回调函数
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(64),unique = True)
	#第一个参数：关系的另一端是哪个模型
	#第二个参数：backref向User模型中添加一个role属性
	users = db.relationship('User',backref = 'role')

	@staticmethod
	def insert_roles():
		admin = Role(id = 1,name = 'Administrator')
		user = Role(id = 2,name = 'User')
		db.session.add(admin)
		db.session.add(user)
		db.session.commit()

	def __repr__(self):
		return self.name



class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(64),unique = True,index = True)
	password_hash = db.Column(db.String(128))
	comments  = db.relationship('Comment',backref = 'user')
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id'),default = 2)
	avtar = db.Column(db.Text)

	@property
	def password(self):
		raise AttributedError('password is not a readable attribute')

	@password.setter
	def password(self,password):
		self.password_hash = generate_password_hash(password)
		
	def verify_password(self,password):
		# print '输入的密码hash:' + generate_password_hash(password)
		# print '数据库中的hash:' + self.password_hash.decode("ascii")
		return check_password_hash(self.password_hash,password)

	def saveUser(self):
		db.session.add(self)
		db.session.commit()

	#类方法
	@staticmethod
	def add_admin():
		adminwaye = User(username = 'adminwayne',password = 'shihoujian1',avtar = '',role_id = 1)
		stranger = User(username = '游客',password = '',avtar = 'http://attach.bbs.miui.com/forum/201111/02/134116q930mdhdn9nhq9f9.jpg',role_id = 2)
		db.session.add(adminwaye)
		db.session.add(stranger)
		db.session.commit()


	#实现flask-login的方法或者集成Usermixin类
	def __repr__(self):
		return self.username

#文章模型
class Post(db.Model):
	"""文章模型"""
	__tablename__ = 'posts'
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.Text)
	cover = db.Column(db.Text)
	summary = db.Column(db.Text)
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime,index = True,default = datetime.now())
	like = db.Column(db.Integer,default = 0)
	tag_id = db.Column(db.Integer,db.ForeignKey('tags.id'))
	comments  = db.relationship('Comment',backref = 'post')

	@property
	def commentsCount(self):
		return len(self.comments)

	def savePost(self):
		db.session.add(self)
		db.session.commit()

	def deletePost(self):
		db.session.delete(self)
		db.session.commit()

	def __repr__(self):
		return self



#评论模型
class Comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer,primary_key = True)
	timestamp = db.Column(db.DateTime,index = True,default = datetime.now())
	content = db.Column(db.Text)
	post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


	def saveComment(self):
		db.session.add(self)
		db.session.commit()


#标签模型
class Tag(db.Model):
	__tablename__ = 'tags'
	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.Text,index = True)
	posts = db.relationship('Post',backref = 'tag')

	def saveTag(self):
		db.session.add(self)
		db.session.commit()


