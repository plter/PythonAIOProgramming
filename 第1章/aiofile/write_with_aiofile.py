"""
第1章/write_with_aiofile.py
"""
import asyncio

import aiofile  # 引入已实现的 aiofile 模块


async def main():
    # 通过异步方式以写文本模式打开 data.txt 文件
    f = await aiofile.open_async("data.txt", "w")
    # 向文件中写入数据
    await f.write("aio file")
    # 关闭文件
    await f.close()


if __name__ == '__main__':
    asyncio.run(main())
