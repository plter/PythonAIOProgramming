import asyncio, aiomysql.sa, sqlalchemy, aiomysql.sa.result

student = sqlalchemy.Table(
    'student', sqlalchemy.MetaData(),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('student_name', sqlalchemy.String(255)),
    sqlalchemy.Column('student_age', sqlalchemy.Integer)
)


async def print_all_data(conn):
    result: aiomysql.sa.result.ResultProxy = await conn.execute(student.select())
    all_data = await result.fetchall()
    print(all_data)


async def main():
    engine: aiomysql.sa.Engine = await aiomysql.sa.create_engine(
        host='127.0.0.1', port=3306, user='root', password='pwd', db='mydb'
    )
    conn: aiomysql.sa.SAConnection = await engine.acquire()

    # 增加一条数据
    await conn.execute(student.insert().values(student_name='杨阳', student_age=20))
    await print_all_data(conn)

    # 修改一条数据
    await conn.execute(student.update().where(student.columns.id == 1).values(student_age=10))
    await print_all_data(conn)

    # 删除一条数据
    await conn.execute(student.delete().where(student.columns.id == 1))
    await print_all_data(conn)
    engine.release(conn)


if __name__ == '__main__':
    asyncio.run(main())
