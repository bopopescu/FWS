# -*- coding: utf-8 -*-


from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from  wtforms.validators import Required



#定义写文章表单
class PostForm(Form):
	body = TextAreaField(u'你此刻的想法...',validators = [Required()])
	submit = SubmitField(u'提交')
		