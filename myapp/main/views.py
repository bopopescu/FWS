# -*- coding: utf-8 -*-
#! /usr/bin/env python


#蓝本中定义程序路由


from datetime import datetime
from flask import render_template,session,redirect,url_for,request
from main import main
from flask.ext.login import login_required
from models import Post,Tag,Comment
from forms import CommentForm

@main.route('/',methods = ['GET','POST'])
def index():
	page = request.args.get('page',1,type = int)
	pagination = Post.query.order_by(Post.id.desc()).paginate(page,per_page = 5,error_out = False)
	posts = pagination.items
	return render_template('index.html',posts = posts,pagination = pagination),200


@main.route('/about',methods = ['GET','POST'])
def about():
	return render_template('about.html'),200


@main.route('/tags',methods = ['GET','POST'])
def tags():
	tags = Tag.query.order_by(Tag.id.desc()).all()
	return render_template('tags.html',tags = tags),200



@main.route('/tagname/<tagname>',methods = ['GET','POST'])
def tagname(tagname):
	tag =  Tag.query.filter_by(name = tagname).first()
	if tag is not None:
		tagid = tag.id
		page = request.args.get('page',1,type = int)
		pagination = Post.query.filter_by(tag_id = tagid).order_by(Post.id.desc()).paginate(page,per_page = 5,error_out = False)
		posts = pagination.items
		return render_template('index.html',posts = posts,pagination = pagination),200
	return render_template('tags.html',tags = tags),200


# @main.route('/like/<postid>',methods = ['GET','POST'])
# def like(postid):
# 	print 'like'
# 	post = Post.query.filter_by(id = postid).first()
# 	if post is not None:
# 		post.like = post.like + 1
# 		post.savePost()
# 	redirectURL = url_for('.index',postid = postid)
# 	return redirect(redirectURL + '#%s' % postid)
	

@main.route('/detail/<int:postid>',methods = ['GET','POST'])
def detail(postid):
	post = Post.query.filter_by(id = postid).first()
	form = CommentForm()
	if form.validate_on_submit():
		comment = Comment(content = form.content.data,post_id = postid,user_id = 3)
		comment.saveComment()
		redirectURL = url_for('.detail',postid = postid)
		return redirect(redirectURL + '#respond')
	return render_template('detail.html',post = post,form = form),200


@main.route('/list',methods = ['GET','POST'])
def list():
	page = request.args.get('page',1,type = int)
	pagination = Post.query.order_by(Post.id.desc()).paginate(page,per_page = 20,error_out = False)
	posts = pagination.items
	return render_template('list.html',posts = posts,pagination = pagination),200	




