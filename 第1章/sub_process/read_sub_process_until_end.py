"""
第1章/sub_process/read_sub_process_until_end.py
"""

import asyncio


async def main():
    # 创建了进程用于执行系统命令 ls
    p = await asyncio.create_subprocess_shell(
        "ls",
        # 将输出信息重定向到子进程管道，而不是直接输出到系统终端，
        # 这样便于后续通过该子进程直接读取数据
        stdout=asyncio.subprocess.PIPE
    )

    # 在没有结束之前一直读取数据， eof 全称 End of file，意为文件结尾，
    # 指该数据的结尾
    while not p.stdout.at_eof():
        # 通过子进程的标准输出管道读取一行内容
        line = await p.stdout.readline()
        if line:
            print(line)


asyncio.run(main())
