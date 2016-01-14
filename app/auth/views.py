# -*- coding: utf-8 -*-


from flask import render_template
from __init__ import auth

@auth.route('/login')
def login():
	#在template文件夹下创建auth文件夹
	return render_template('auth/login.html')