"""
第8章/pydal_example/app.py
"""

from pydal import DAL, Field

# if __name__ == '__main__':
#     db = DAL("mysql://root:rootpw@127.0.0.1/mydb")
#     db.define_table(
#         'student',
#         Field('name'),
#         Field('age')
#     )
#     db.student.insert(
#         name="小云",
#         age="20"
#     )
#     db.commit()
#     all_students = db(db.student.id > 0).select()
#     print(all_students)
#     pass

if __name__ == '__main__':
    # 连接数据库，默认将使用SQLite数据库引擎，将
    # 生成 dummy.db 文件，如果要修改保存的文件
    # 名为 data.db，写法如：DAL("sqlite://data.db")
    db = DAL()
    # 定义名为 student 的表，pyDAL会自动生成
    # 自增 id 列
    db.define_table(
        'student',
        Field('name'),
        Field('age')
    )
    # 向 student 表中插入一条数据
    db.student.insert(
        name="小云",
        age="20"
    )
    # 将数据保存
    db.commit()
    # 从 student 表中查询出所有数据
    all_students = db(db.student.id > 0).select()
    print(all_students)
    pass
