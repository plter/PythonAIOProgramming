"""
第3章/aiohttp_route/pages.py
"""
from aiohttp import web

routes = web.RouteTableDef()


@routes.get(r'/p/{page_id:\d+}')
async def page(req: web.Request):
    return web.Response(text=f"Page id is {req.match_info['page_id']}")


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
