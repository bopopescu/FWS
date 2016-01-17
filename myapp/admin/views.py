# -*- coding: utf-8 -*-

from flask import render_template,redirect,url_for
from admin import admin
from admin.forms import Postform
from models import Post,Tag
from flask.ext.login import logout_user,login_required


@admin.route('/post',methods = ['GET','POST'])
@login_required
def post():
	form = Postform()
	if form.validate_on_submit():
		#先查询标签是否存在
		tag = Tag.query.filter_by(name = form.tag.data.encode('utf-8')).first()
		if tag is None:
			tag = Tag(name = form.tag.data.encode('utf-8'))
			tag.saveTag()

		post = Post(title = form.title.data.encode('utf-8'),
					tag_id = tag.id,
					body = form.body.data.encode('utf-8'),
					cover = form.cover.data.encode('utf-8'))
		post.savePost()
		return render_template('admin/sucess.html'),200
	return render_template('admin/post.html',form = form),200
