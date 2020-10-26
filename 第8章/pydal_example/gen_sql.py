"""
第8章/pydal_example/gen_sql.py
"""
from pydal import DAL, Field

if __name__ == '__main__':
    db = DAL("mysql://root:rootpw@127.0.0.1/mydb")
    db.define_table(
        'student',
        Field('name'),
        Field('age')
    )
    # 在相应的语句前添加下划线用于生成SQL语句而不执行
    sql = db.student._insert(
        name="小云", age="20"
    )
    print(sql)

    sql = db(db.student.id == 2)._update(
        name="小明", age="10"
    )
    print(sql)

    sql = db(db.student.id > 0)._select()
    print(sql)

    sql = db(db.student.id == 1)._delete()
    print(sql)
