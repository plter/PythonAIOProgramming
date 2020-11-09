"""
第3章/aiohttp_submitform/server.py
"""
from aiohttp import web
import jinja2
import aiohttp_jinja2
import os

APP_ROOT = os.path.dirname(__file__)
app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "tpls"))
)
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template("index.html")
async def index(request: web.Request):
    return dict(title="首页")


@routes.post("/login")
@aiohttp_jinja2.template("login.html")
async def login(request: web.Request):
    # 读取表单数据
    user = await request.post()
    return dict(title="登录结果", user=user)


app.add_routes(routes)
app.router.add_static("/node_modules", os.path.join(APP_ROOT, "node_modules"))
web.run_app(app)
