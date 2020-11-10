"""
第4章/aiohttp_mysql/config.py
"""
import os

# 服务器根目录
SERVER_ROOT = os.path.dirname(__file__)

# 所有静态文件目录
STATIC_MAPPING = [
    dict(
        web_path="/node_modules",
        dir=os.path.join(SERVER_ROOT, "node_modules")
    ),
    dict(
        web_path="/static",
        dir=os.path.join(SERVER_ROOT, "static")
    )
]

# 模板文件根目录
TEMPLATE_ROOT = os.path.join(SERVER_ROOT, "tpls")

# 数据库连接相关配置信息
DB_HOST = 'db'
DB_PORT = 3306
DB_NAME = 'mydb'
DB_USER = 'root'
DB_PASSWORD = 'pwd'
