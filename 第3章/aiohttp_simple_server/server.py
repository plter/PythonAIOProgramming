"""
第3章/aiohttp_simple_server/server.py
"""
from aiohttp import web


# 请求处理函数，接受一个参数为请求对象，返回信息将被传给浏览器端
async def hello(request: web.Request):
    return web.Response(text="Hello, world")


# 创建一个服务器应用
app = web.Application()
# 将 hello 处理函数映射到网站根路径 /
app.router.add_get("/", hello)
# 启动服务器应用
web.run_app(app)
