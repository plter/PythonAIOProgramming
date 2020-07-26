import asyncio


async def main():
    p = await asyncio.create_subprocess_shell("ls")
    await p.wait()


asyncio.run(main())
