from aiohttp import web
from db import with_db
from aiomysql.sa import SAConnection, result
import aiohttp_jinja2, jinja2, config, tables

routes = web.RouteTableDef()


@routes.get('/')
@aiohttp_jinja2.template("index.html")
@with_db
async def index(req, db: SAConnection):
    exec_result: result.ResultProxy = await db.execute(tables.student.select())
    data = await exec_result.fetchall()
    return dict(students=data, title="学生列表")


@routes.get('/edit')
@aiohttp_jinja2.template("edit.html")
@with_db
async def edit(req: web.Request, db: SAConnection):
    student_id = req.query.getone("id") if "id" in req.query else None
    student = None
    if student_id:  # 如果页面有传入student_id，则启用编辑，否则执行添加操作
        student_result: result.ResultProxy = await db.execute(
            tables.student.select().where(tables.student.columns.id == student_id)
        )
        student = await student_result.fetchone()
    return dict(title="编辑", student=student)


@routes.post('/edit')
@with_db
async def edit(req: web.Request, db: SAConnection):
    params = await req.post()
    student_name = params['student_name'] if "student_name" in params else None
    student_age = params['student_age'] if "student_age" in params else None
    student_id = params['student_id'] if "student_id" in params else None
    if not student_name or not student_age:
        return web.Response(text="Parameters error")
    if student_id:  # 如果有 student_id，则尝试查找这条数据
        ret: result.ResultProxy = await db.execute(
            tables.student.select().where(tables.student.columns.id == student_id)
        )
        if ret.rowcount:  # 如果存在这条记录，更新这条记录
            conn = await db.begin()
            await db.execute(
                tables.student.update()
                    .where(tables.student.columns.id == student_id)
                    .values(student_name=student_name, student_age=student_age)
            )
            await conn.commit()
            raise web.HTTPFound("/")
    # 能够执行到这里，说明指定student_id的记录不存在或者没有指定student_id，则执行添加新数据操作
    conn = await db.begin()
    await db.execute(
        tables.student.insert()
            .values(student_name=student_name, student_age=student_age)
    )
    await conn.commit()
    raise web.HTTPFound("/")


@routes.get('/remove')
@with_db
async def remove(req: web.Request, db: SAConnection):
    student_id = req.query.getone("id") if "id" in req.query else None
    if student_id:
        conn = await db.begin()
        await db.execute(  # 根据student_id删除数据
            tables.student.delete().where(tables.student.columns.id == student_id)
        )
        await conn.commit()
        raise web.HTTPFound("/")
    else:
        return web.Response(text="Parameters error")


if __name__ == '__main__':
    app = web.Application()
    # 配置模板文件根目录
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(config.TEMPLATE_ROOT)
    )
    app.add_routes(routes)
    # 配置静态文件目录
    for m in config.STATIC_MAPPING:
        app.router.add_static(m['web_path'], m['dir'])
    web.run_app(app, port=8000)
