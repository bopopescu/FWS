# -*- coding: utf-8 -*-

from flask import Blueprint

#通过实例化Blueprint类对象来创建蓝本。
#两个参数：蓝本的名字和蓝本所在的包或模块。

main = Blueprint('main',__name__)

#导入views和errors就能把路由和错误处理程序与蓝本关联起来
#这些模块在脚本的末尾导入，是为了避免循环导入依赖，因为在views.py和errors.py中还要导入蓝本main
import views,errors
