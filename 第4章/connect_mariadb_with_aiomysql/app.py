"""
第4章/connect_mariadb_with_aiomysql/app.py
"""
import asyncio, aiomysql


async def main():
    # 建立与数据库的连接
    conn: aiomysql.Connection = await aiomysql.connect(
        host='127.0.0.1', port=3306, user='root',
        password='pwd', db='mydb'
    )
    # 创建一个 cursor 对象用于操作数据库
    cur: aiomysql.Cursor = await conn.cursor()
    # 执行一条 sql 语句，返回值是影响的数据的条数
    effected = await cur.execute(
        "INSERT INTO `student` (`student_name`, `student_age`) "
        "VALUES ('小云', 10);"
    )
    print(effected)
    # 将更改提交到数据库
    await conn.commit()
    # 关闭 cursor 对象
    await cur.close()
    # 关闭连接对象
    conn.close()


if __name__ == '__main__':
    asyncio.run(main())
