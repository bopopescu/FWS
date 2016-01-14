# -*- coding: utf-8 -*-

from flask import render_template,redirect,url_for
from admin import admin
from admin.forms import Postform
from models import Post


@admin.route('/post',methods = ['GET','POST'])
def post():
	form = Postform()
	if form.validate_on_submit():
		post = Post(title = u'手动插入'.encode('utf-8'),body = u'手动插入'.encode('utf-8'))
		post.savePost()
		return post.title
	return render_template('admin/post.html',form = form),200
