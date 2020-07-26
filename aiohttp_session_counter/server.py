from aiohttp import web
import aiohttp_session

routes = web.RouteTableDef()


@routes.get('/')
async def index(request: web.Request):
    session = await aiohttp_session.get_session(request)
    session['count'] = (session['count'] if 'count' in session else 0) + 1
    return web.Response(text=f"Count is {session['count']}")


app = web.Application()
app.add_routes(routes)
aiohttp_session.setup(app, aiohttp_session.SimpleCookieStorage())
web.run_app(app)
