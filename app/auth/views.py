# -*- coding: utf-8 -*-


from flask import render_template,redirect
from __init__ import auth
from forms import AdminLoginForm
from models import User,Role,Post
from flask.ext.login import logout_user,login_required


@auth.route('/login',methods = ['GET','POST'])
def login():
	#在template文件夹下创建auth文件夹
	form = AdminLoginForm()
	if form.validate_on_submit():

		user = User.query.filter_by(username = '123').first()

		if user is not None and user.verify_password(form.password.data):
			#成功
			login_user = (user,form.remember_me.data)
			return redirect(request.args.get('next')) or url_for('main.index')
		flash(u'错误的用户名或密码')
		print "错误的用户名或密码"
	return render_template('auth/login.html',form = form),200


@auth.route('/logout',methods = ['GET','POST'])
@login_required
def logout():
	logout_user()
	flash(u'你已经登出')
	return redirect(url_for('main.index')),200