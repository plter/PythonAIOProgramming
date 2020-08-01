import os

SERVER_ROOT = os.path.dirname(__file__)
STATIC_MAPPING = [
    dict(web_path="/node_modules", dir=os.path.join(SERVER_ROOT, "node_modules")),
    dict(web_path="/static", dir=os.path.join(SERVER_ROOT, "static"))
]
TEMPLATE_ROOT = os.path.join(SERVER_ROOT, "tpls")

DB_HOST = 'db'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'pwd'
DB_NAME = 'mydb'
