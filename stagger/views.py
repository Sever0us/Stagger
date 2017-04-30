from pyramid.view import view_config, view_defaults


@view_defaults(renderer='templates/navBar.jinja2')
class homeViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'page':'Home'}