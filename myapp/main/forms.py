# -*- coding: utf-8 -*-

#登录表单


from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from  wtforms.validators import Required,Length


#发布评论表单
class CommentForm(Form):
	content = TextAreaField(u'输入你的评论',validators = [Required()])
	submit = SubmitField(u'发表评论')
