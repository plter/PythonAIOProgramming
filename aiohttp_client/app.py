import asyncio, time

import aiohttp


async def main():
    session = aiohttp.ClientSession(
        # 使用最简单的 Cookie 机制
        cookie_jar=aiohttp.CookieJar(unsafe=True)
    )
    for i in range(10):
        response = await session.get('http://127.0.0.1:8080')
        print(f"[{time.strftime('%X')}] {await response.text()}")
        # 每次请求后休眠 1 秒钟
        await asyncio.sleep(1)
    await session.close()


if __name__ == '__main__':
    asyncio.run(main())
