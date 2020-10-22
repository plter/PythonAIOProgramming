"""
第8章/cms4py_first_generation/app/controllers/default.py
"""


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
