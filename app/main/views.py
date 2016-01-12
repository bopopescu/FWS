# -*- coding: utf-8 -*-
#! /usr/bin/env python


#蓝本中定义程序路由


from datetime import datetime
from flask import render_template,session,redirect,url_for
from main.__init__ import main
# from forms import PostForm


@main.route('/',methods = ['GET','POST'])
def index():
	return render_template('index.html'),200

@main.route('/user/<name>')
def user(name):
	return render_template('user.html',name = name),200