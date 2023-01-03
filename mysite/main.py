import aiohttp_jinja2
import jinja2
from aiohttp import web

from mysite.routes import setup_routes

app = web.Application()
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader('mysite/templates'))
setup_routes(app)

if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=7070)
