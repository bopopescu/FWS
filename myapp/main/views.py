# -*- coding: utf-8 -*-
#! /usr/bin/env python


#蓝本中定义程序路由


from datetime import datetime
from flask import render_template,session,redirect,url_for
from main import main
from flask.ext.login import login_required
from models import Post



@main.route('/',methods = ['GET','POST'])
def index():
	posts = Post.query.order_by(Post.timestamp.desc()).all()
	return render_template('index.html',posts = posts),200




