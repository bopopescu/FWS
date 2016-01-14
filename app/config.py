# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is waynezxcvs secretkey'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	WAYNEZXCV_ADMIN = os.environ.get('WAYNEZXCV_ADMIN')
	
	@staticmethod
	def init_app(app):
		print 'init config'

#开发环境
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+mysqlconnector://root:password@localhost:3306/waynezxcv'

#测试环境
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql+mysqlconnector://root:password@localhost:3306/waynezxcv'

#生产环境
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+mysqlconnector://root:password@localhost:3306/waynezxcv'


config = {
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	'default':DevelopmentConfig
}
		