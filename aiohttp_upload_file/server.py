from aiohttp import web
import os, datetime, aiofile, aiohttp_jinja2, jinja2

APP_ROOT = os.path.dirname(__file__)
app = web.Application()
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "tpls"))
)
routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template("index.html")
async def index(request: web.Request):
    return dict(title="首页")


@routes.post("/upload")
@aiohttp_jinja2.template("upload.html")
async def login(request: web.Request):
    # 解析前端上传的数据
    data = await request.post()
    # 根据表单字段名从上传数据中取得文件对象，与 <input name="file"> 对应
    file_object = data['file']
    # 用当前时间当做要保存的文件名
    file_name = f"{datetime.datetime.now().timestamp()}"
    # 以写入二进制数据（wb）的方式打开文件
    file = await aiofile.open_async(os.path.join(APP_ROOT, "uploads", file_name), "wb")
    # 将数据读取出来并保存到目标文件中
    await file.write(file_object.file.read())
    # 关闭文件IO
    await file.close()
    # 将该文件在网站中的路径传给模板
    return dict(title="上传结果", file_path=f"/uploads/{file_name}")


app.add_routes(routes)
app.router.add_static("/node_modules", os.path.join(APP_ROOT, "node_modules"))
app.router.add_static("/uploads", os.path.join(APP_ROOT, "uploads"))
web.run_app(app)
