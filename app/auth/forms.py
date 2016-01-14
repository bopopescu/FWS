# -*- coding: utf-8 -*-

#登录表单


from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from  wtforms.validators import Required,Length


#管理员登录表单
class AdminLoginForm(Form):
	username = StringField(u'用户名',validators = [Required()])
	password = PasswordField(u'密码',validators = [Required()])
	remember_me = BooleanField(u'记住我')
	submit = SubmitField(u'登录')


