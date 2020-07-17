import asyncio


async def main():
    loop = asyncio.get_running_loop()
    f = await loop.run_in_executor(None, open, "data.txt", 'w')
    await loop.run_in_executor(None, f.write, "aio file")
    await loop.run_in_executor(None, f.close)


if __name__ == '__main__':
    asyncio.run(main())
