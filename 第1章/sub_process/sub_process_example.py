"""
第1章/sub_process/sub_process_example.py
"""

import asyncio


async def main():
    # 创建了进程用于执行系统命令 ls
    p = await asyncio.create_subprocess_shell("ls")
    # 等待该进程执行完毕
    await p.wait()


asyncio.run(main())
