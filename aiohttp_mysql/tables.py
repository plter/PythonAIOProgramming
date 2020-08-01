import sqlalchemy

student = sqlalchemy.Table(
    'student', sqlalchemy.MetaData(),
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('student_name', sqlalchemy.String(255)),
    sqlalchemy.Column('student_age', sqlalchemy.Integer)
)
