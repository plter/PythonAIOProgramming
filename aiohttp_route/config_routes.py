from aiohttp import web


async def hello(request: web.Request):
    return web.Response(text="Hello, world")


async def users(req):
    return web.Response(text="All users are here")


app = web.Application()
app.add_routes([
    web.get("/", hello),
    web.get("/users", users)
])
web.run_app(app)
