# -*- coding: utf-8 -*-


from flask import Flask
from flask import make_response
from flask import redirect
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
# manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment()

class NameForm(Form):
	name = StringField(u'用户名',validators = [Required()])
	password = PasswordField(u'密码',validators = [Required()])
	submit = SubmitField(u'登录')



#指定自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),400

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

####
@app.route('/index')
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data= ''
	return render_template('index.html',form=form,name=name)

@app.route('/base')
def basepage():
	return render_template('base.html')


@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)


if __name__ == '__main__':
	app.run(debug=True)