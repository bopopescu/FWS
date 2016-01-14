# -*- coding: utf-8 -*-

from flask import render_template,redirect,url_for
from admin import admin
from admin.forms import Postform
from models import Post


@admin.route('/post',methods = ['GET','POST'])
def post():
	form = Postform()
	if form.validate_on_submit():
		body = form.body.data.encode('utf-8')
		post = Post(title = form.title.data.encode('utf-8'),body = body)
		post.savePost()
		return render_template('admin/sucess.html'),200
	return render_template('admin/test.html',form = form),200
