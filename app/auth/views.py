# -*- coding: utf-8 -*-


from flask import render_template
from __init__ import auth
from forms import AdminLoginForm



@auth.route('/login')
def login():
	#在template文件夹下创建auth文件夹
	form = AdminLoginForm()
	return render_template('auth/login.html',form = form)