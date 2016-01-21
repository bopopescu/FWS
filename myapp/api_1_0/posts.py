# -*- coding: utf-8 -*-



from flask.ext.restful import Resource,Api
from models import Post
import json


class Posts(Resource):
	def get(self,page):
		pagination = Post.query.order_by(Post.id.desc()).paginate(page,per_page = 5)
		posts = pagination.items
		results = []
		for post in posts:
			title = post.title
			tag = post.tag.name
			cover = post.cover
			body = post.body
			summary = post.summary
			article = {
				'title':title,
				'tag':tag,
				'cover':cover,
				'summary':summary,
				'body':body}
			results.append(article)	
		return json.dumps(results)


