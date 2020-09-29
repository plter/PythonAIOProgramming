"""
第1章/sub_process/decode_sub_process_out.py
"""

import asyncio


async def main():
    # 创建了进程用于执行系统命令 ls
    p = await asyncio.create_subprocess_shell(
        "dir",
        stdout=asyncio.subprocess.PIPE
    )

    # 使用communicate函数与子进程通信，并等待子进程结束，在子进程
    # 结束后获得子进程的输出信息
    stdout, stderr = await p.communicate()
    # 将信息以gbk（gb2312是简体中文，gbk同时兼容简体中文与繁体中文）
    # 的编码方式解码成字符串并输出
    print(stdout.decode("gbk"))


asyncio.run(main())
