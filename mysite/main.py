"""
The module creates an application instance of aiohttp-server
with routes and handling of static files
"""
import aiohttp_jinja2
import jinja2
from aiohttp import web
from mysite.routes import setup_routes

# create aiohttp server instance
app = web.Application()
# connect templates-folder to jinja2
aiohttp_jinja2.setup(app,
                     loader=jinja2.FileSystemLoader('mysite/templates'))
setup_routes(app)
# add route for static-files
app.router.add_static("/static/", path="mysite")
# run app
if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=7070)
