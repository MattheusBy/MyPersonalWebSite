"""
The module sets appropriate URL for views-functions
"""

from mysite.views import index, chistolife


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/4istolife', chistolife)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path='mysite/static',
                          name='static')