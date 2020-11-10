"""
第4章/aiohttp_mysql/db.py
"""
from aiomysql.sa import create_engine, Engine
import config

file_scope_vars = {}


async def get_engine():
    """
    获取数据库引擎单例
    :return:
    """
    if "engine" not in file_scope_vars:
        file_scope_vars['engine'] = await create_engine(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            db=config.DB_NAME
        )
    return file_scope_vars['engine']


def with_db(fun):
    """
    用于给请求处理函数添加数据库支持的装饰器函数
    :param fun:
    :return:
    """

    async def wrapper(req):
        # 获取数据库引擎
        engine: Engine = await get_engine()
        # 创建一个数据库连接实例
        db = await engine.acquire()
        try:
            result = await fun(req, db)
            # 执行结束后释放数据库连接
            engine.release(db)
            return result
        except Exception as e:
            # 捕获异常后释放数据库连接
            engine.release(db)
            raise e

    return wrapper
