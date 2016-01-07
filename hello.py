# -*- coding: utf-8 -*-

#

from flask import Flask
from flask import make_response
from flask import redirect
from flask.ext.script import Manager
from flask import render_template
from flask.ext.bootstrap import Bootstrap



app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

#指定自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),400

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

@app.route('/base')
def basepage():
	return render_template('base.html')

@app.route('/')
def index():
	# response = make_response('<h1> hello ,world </h1><br><br/><p> apple <p/>',200)
	# return redirect('http://www.baidu.com')
	return render_template('index.html')


@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)





















if __name__ == '__main__':
	manager.run()