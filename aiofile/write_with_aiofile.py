import asyncio

import aiofile


async def main():
    f = await aiofile.open_async("data.txt", "w")
    await f.write("aio file")
    await f.close()


if __name__ == '__main__':
    asyncio.run(main())
