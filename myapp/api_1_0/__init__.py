# -*- coding: utf-8 -*-

#API V 1.0

from flask import Blueprint
from flask.ext.restful import Api



api_1_0_bp = Blueprint('api_1_0_bp',__name__)
api = Api(api_1_0_bp)


import authentication
from posts import Posts

api.add_resource(Posts,'/posts/<int:page>')
