# -*- coding: utf-8 -*-

from flask import render_template,redirect,url_for
from admin import admin
from admin.forms import Postform
from models import Post


@admin.route('/post',methods = ['GET','POST'])
def post():
	form = Postform()
	if form.validate_on_submit():
		post = Post(title = form.title.data.encode('utf-8'),body = form.body.data.encode('utf-8'))
		post.savePost()
		print form.title.data,form.body.data
		return render_template('admin/sucess.html'),200
	print '发布失败。。。',form.body.data	
	return render_template('admin/post.html',form = form),200
