"""
第5章/quart_app/server.py
"""
from quart import Quart

# 创建一个Quart应用
app = Quart(__name__)


# 处理对站点根路径的请求
@app.route('/')
async def hello():
    # 向前端返回字符串
    return 'hello'


app.run()
