from quart import Quart

app = Quart(__name__)  # 创建一个Quart应用


@app.route('/')  # 处理对站点根路径的请求
async def hello():
    return 'hello'  # 向前端返回字符串
