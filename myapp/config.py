# -*- coding: utf-8 -*-

import os
import sys

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or ''
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	WAYNEZXCV_ADMIN = os.environ.get('')
	
	@staticmethod
	def init_app(app):
		print 'init config'

#开发环境
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or ''

#测试环境
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or ''

#生产环境
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or ''


config = {
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'production':ProductionConfig,
	'default':DevelopmentConfig
}
		