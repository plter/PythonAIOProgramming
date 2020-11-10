import asyncio


async def shell(cmd):
    await (await asyncio.subprocess.create_subprocess_shell(cmd)).wait()


async def main():
    await shell("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple aiomysql")


if __name__ == '__main__':
    asyncio.run(main())
