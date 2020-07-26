from aiohttp import web
import os

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes(routes)
# 配置一个静态文件目录
app.router.add_static(
    "/static",
    os.path.join(os.path.dirname(__file__), 'static')
)
web.run_app(app)
