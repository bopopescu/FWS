# -*- coding: utf-8 -*-


from flask import Flask
from flask import make_response
from flask.ext.script import Manager
from flask import render_template,session,redirect,url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)



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
@app.route('/',methods= ['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session['name']
		if old_name is not None and old_name != form.name.data:
			flash(u'looks your changed your name')#仅调用flash（）并不能把消息显示出来。需要在模板中渲染Flash消息
		session['name'] = form.name.data #相当于NSUserDefaluts.像dict一样使用它
		return redirect(url_for('index'))#redirect()重定向  url_for()传入端点名。即响应视图函数的函数名
	return render_template('index.html',form=form,name=session['name'])


@app.route('/base')
def basepage():
	return render_template('base.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

if __name__ == '__main__':
	app.run(debug=True)