from pyramid.view import view_config

@view_config(route='home', renderer='pyramid_blogr:templates/index.jinja2')
def index_page(request):
	return {}

@view_config(route_name='auth', match_param='action=in', renderer='string', request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string', request_method='POST')
def sign_in_out(request):
	return {}