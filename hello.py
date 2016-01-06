# -*- coding: utf-8 -*-

#

from flask import Flask
from flask import make_response
from flask import redirect
from flask.ext.script import Manager
from flask import render_template

app = Flask(__name__)
manager = Manager(app)






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