from aiohttp import web


async def hello(request: web.Request):
    return web.Response(text="Hello, world")


app = web.Application()
app.router.add_get("/", hello)
web.run_app(app)
