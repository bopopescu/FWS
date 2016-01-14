# -*- coding: utf-8 -*-
#! /usr/bin/env python


#蓝本中定义程序路由


from datetime import datetime
from flask import render_template,session,redirect,url_for
from main import main
from flask.ext.login import login_required



@main.route('/',methods = ['GET','POST'])
def index():
	return render_template('index.html'),200



