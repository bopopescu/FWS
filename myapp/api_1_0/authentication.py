# -*- coding: utf-8 -*-



from flask.ext.httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username,password):
	if username == '':
		g.current_user = AnonymousUser()
		return True


