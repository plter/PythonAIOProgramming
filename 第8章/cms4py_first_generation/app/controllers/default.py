"""
第8章/cms4py_first_generation/app/controllers/default.py
"""
from cms4py.cache import cache


async def index(req, res):
    await res.end(b"Home page")
    pass


class hello:
    """
    如果 action 是类，则需要使用魔术函数 __call__ 重载函数调用
    运算符以接受调用操作
    """

    async def __call__(self, req, res):
        await res.end(b"Hello cms4py")


@cache(expire=5)
async def cached_page(req, res):
    await res.end(b"Cached page")


async def get_args(req, res):
    arg0 = req.arg(0)
    await res.write(b"Arg0 is ")
    await res.end(arg0.encode("utf-8") if arg0 else b"None")
