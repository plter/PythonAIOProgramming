"""
第4章/aiomysql_crud/simple_query.py
"""

import asyncio, aiomysql


async def main():
    # 创建连接池
    pool: aiomysql.Pool = await aiomysql.create_pool(
        minsize=0, maxsize=10,
        host='127.0.0.1', port=3306, user='root',
        password='pwd', db='mydb'
    )
    # 启用一个连接
    conn: aiomysql.Connection = await pool.acquire()
    # 创建一个 cursor 对象用于操作数据库
    cur: aiomysql.Cursor = await conn.cursor()

    await cur.execute(
        "SELECT * FROM `student` WHERE `id` = '1';"
    )
    print(cur.description)
    print(await cur.fetchall())
    # 关闭 cursor 对象
    await cur.close()
    # 释放一个连接
    pool.release(conn)
    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
