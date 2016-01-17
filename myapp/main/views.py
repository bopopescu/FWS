# -*- coding: utf-8 -*-
#! /usr/bin/env python


#蓝本中定义程序路由


from datetime import datetime
from flask import render_template,session,redirect,url_for,request
from main import main
from flask.ext.login import login_required
from models import Post,Tag



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


@main.route('/like/<postid>')
def like():
	print 'like'
	post = Post.query.filter_by(id = postid).first()
	if post is not None:
		post.like = post.like + 1
		post.savePost()

