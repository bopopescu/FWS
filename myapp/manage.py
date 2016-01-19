#! /usr/bin/env python
# -*- coding: utf-8 -*-



import os
from __init__ import create_app,db
from models import User,Role,Post
from flask.ext.script import Manager,Shell,Server
from flask.ext.migrate import Migrate,MigrateCommand




app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)


#创建shell命令上下文。。这里的app，db等无需手动在shell中import
def make_shell_context():
	return dict(app = app,db = db,User = User,Role = Role,Post = Post)

@manager.command
def deploy():
	"Run deployment tasks"
	from flask.ext.migrate import upgrade
	from models import User,Role,Post

	#数据库迁移到最新修订版本
	# upgrade()

	#创建用户角色
	Role.insert_roles()

	#创建管理员账号
	User.add_admin()

#添加shell命令
manager.add_command("shell",Shell(make_context = make_shell_context))
manager.add_command('db',MigrateCommand)




if __name__ == '__main__':
	manager.run()