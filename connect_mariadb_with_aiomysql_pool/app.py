import asyncio, aiomysql


async def main():
    # 创建连接池
    pool: aiomysql.Pool = await aiomysql.create_pool(
        minsize=0, maxsize=10,
        host='127.0.0.1', port=3306, user='root', password='pwd', db='mydb'
    )

    conn: aiomysql.Connection = await pool.acquire()  # 启用一个连接
    cur: aiomysql.Cursor = await conn.cursor()  # 创建一个 cursor 对象用于操作数据库
    effected = await cur.execute(  # 执行一条 sql 语句，返回值是影响的数据的条数
        "INSERT INTO `student` (`student_name`, `student_age`) VALUES ('小云', 10);"
    )
    print(effected)

    await conn.commit()  # 将更改提交到数据库
    await cur.close()  # 关闭 cursor 对象
    pool.release(conn)  # 释放一个连接
    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
