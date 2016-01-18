# -*- coding: utf-8 -*-

#发表文章表单


from flask.ext.wtf import Form
from wtforms import StringField,TextAreaField,SubmitField
from  wtforms.validators import Required,Length


class Postform(Form):
	title = StringField(u'标题',validators = [Required()])
	body = TextAreaField(u'内容',validators = [Required()])
	tag = StringField(u'标签',validators = [Required()])
	cover = StringField(u'封面')
	summary = TextAreaField(u'简介',validators = [Required()])
	submit = SubmitField(u'发布')


