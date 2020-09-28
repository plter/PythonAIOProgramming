"""
第1章/sub_process/sub_process_exec.py
"""

import asyncio


async def main():
    # 创建了进程用于执行系统命令 ls
    p = await asyncio.create_subprocess_exec(
        # 文件路径可以换成任何本机真实存在的可执行程序的全路径。
        "/Users/yunp.top/Work/tools/ffmpeg",
        # 将输出信息重定向到子进程管道，而不是直接输出到系统终端，
        # 这样便于后续通过该子进程直接读取数据
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # 在没有结束之前一直读取数据， eof 全称 End of file，意为文件结尾，
    # 指该数据的结尾
    while not p.stderr.at_eof():
        # 通过子进程的标准输出管道读取一行内容
        line = await p.stderr.readline()
        if line:
            print(line)


asyncio.run(main())
