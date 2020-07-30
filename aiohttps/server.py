from aiohttp import web
import ssl, os

routes = web.RouteTableDef()


@routes.get('/')
async def index(request: web.Request):
    return web.Response(text="Hello World")


app = web.Application()
app.add_routes(routes)
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# 加载网站证书文件
ssl_context.load_cert_chain(
    os.path.join(os.path.dirname(__file__), "ssl", "cert.pem"),
    os.path.join(os.path.dirname(__file__), "ssl", "cert.key"),
)
web.run_app(app, port=443, ssl_context=ssl_context)
