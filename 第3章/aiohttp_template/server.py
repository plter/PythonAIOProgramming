"""
第3章/aiohttp_template/server.py
"""

from aiohttp import web
import jinja2
import aiohttp_jinja2
import os

app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), "tpls")
    )
)
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template("index.html")
async def hello(request):
    return dict(name="小云", age=21)


app.add_routes(routes)
web.run_app(app)
