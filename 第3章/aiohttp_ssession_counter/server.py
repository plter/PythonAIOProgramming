"""
第3章/aiohttp_ssession_counter/server.py
"""
import base64

from aiohttp import web
from aiohttp_session import setup, get_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

routes = web.RouteTableDef()


@routes.get('/')
async def index(request: web.Request):
    session = await get_session(request)
    session['count'] = \
        (session['count'] if 'count' in session else 0) + 1
    return web.Response(text=f"Count is {session['count']}")


app = web.Application()
app.add_routes(routes)
fernet_key = fernet.Fernet.generate_key()
# secret_key 必须是 url安全的、base64 编码的32字节数据
# url安全是指不能包括 '+' 与 '/' ，会使用 '-' 代替 '+'，'_' 代替 '/'
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))
web.run_app(app)
