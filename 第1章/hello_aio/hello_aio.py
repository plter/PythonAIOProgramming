"""
第1章/hello_aio.py
"""

import asyncio
import time


# 使用 async 关键字声明一个异步函数
async def main():
    print(f"{time.strftime('%X')} Hello")
    # 使用 await 关键字休眠当前协程
    await asyncio.sleep(1)
    print(f"{time.strftime('%X')} World")


asyncio.run(main())
