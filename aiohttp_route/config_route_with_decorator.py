from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@routes.post('/save_user_info')
async def save_user_info(req):
    return web.Response(text="Saved")


app = web.Application()
app.add_routes(routes)
web.run_app(app)
