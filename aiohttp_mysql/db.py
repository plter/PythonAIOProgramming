from aiomysql.sa import create_engine, Engine
import config

file_scope_vars = {}


async def get_engine():
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
    async def wrapper(req):
        engine: Engine = await get_engine()
        db = await engine.acquire()
        try:
            result = await fun(req, db)
            engine.release(db)
            return result
        except Exception as e:
            engine.release(db)
            raise e

    return wrapper
