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
					cover = form.cover.data.encode('utf-8'),
					summary = form.summary.data.encode('utf-8'))
		post.savePost()
		return render_template('admin/sucess.html'),200
	return render_template('admin/post.html',form = form),200


@admin.route('/manage',methods = ['GET','POST'])
@login_required
def manage():
	posts = Post.query.order_by(Post.id.desc()).all()
	return render_template('admin/manage.html',posts = posts),200


@admin.route('/manage/delete/<postid>',methods = ['GET','POST'])
@login_required
def delete(postid):
	print 'delete : %s' % postid
	post = Post.query.filter_by(id = postid).first()
	if post is not None:
		post.deletePost()
		return render_template('admin/sucess.html'),200
	return redirect(url_for('admin.manage')),200
	
