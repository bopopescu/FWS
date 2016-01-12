# -*- coding: utf-8 -*-

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment 
from flask.ext.sqlalchemy import SQLAlchemy 
from config import config

#初始化bootstrap
bootstrap = Bootstrap()
#初始化Mail
mail = Mail()
#初始化Moment
moment = Moment()
#初始化SQLAlchemy
db = SQLAlchemy()

#工厂方法创建程序实例
def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)

	#路由和自定义的错误页面处理
	from main.__init__ import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app