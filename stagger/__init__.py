from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.scan('.views')
    config.add_static_view(name='static', path='stagger:static')

    return config.make_wsgi_app()