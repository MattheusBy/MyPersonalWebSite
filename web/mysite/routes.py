"""
The module sets appropriate URL for views-functions
"""

from mysite.views import index, chistolife, djangomarket, mypersonalwebsite, apiwallet


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/4istolife', chistolife)
    app.router.add_get('/djangomarket', djangomarket)
    app.router.add_get('/mypersonalwebsite', mypersonalwebsite)
    app.router.add_get('/apiwallet', apiwallet)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path='mysite/static',
                          name='static')
