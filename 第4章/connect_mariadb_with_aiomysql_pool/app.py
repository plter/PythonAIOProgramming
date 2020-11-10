"""
第4章/connect_mariadb_with_aiomysql_pool/app.py
"""
import asyncio, aiomysql


async def main():
    # 创建一个连接池，允许的最大连接数是10，最小连接数是0
    pool: aiomysql.Pool = await aiomysql.create_pool(
        minsize=0, maxsize=10,
        host='127.0.0.1', port=3306, user='root',
        password='pwd', db='mydb'
    )

    # 通过连接池启用一个连接，如果当前连接池已满，则等待其它
    # 连接被释放后再建立连接
    conn: aiomysql.Connection = await pool.acquire()
    # 创建一个 cursor 对象用于操作数据库
    cur: aiomysql.Cursor = await conn.cursor()
    # 执行一条 sql 语句，返回值是影响的数据的条数
    effected = await cur.execute(
        "INSERT INTO `student` (`student_name`, `student_age`) "
        "VALUES ('小云', 10);"
    )
    print(effected)

    await conn.commit()  # 将更改提交到数据库
    await cur.close()  # 关闭 cursor 对象
    pool.release(conn)  # 在使用完毕后释放该连接
    pool.close()
    await pool.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
