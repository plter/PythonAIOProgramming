"""
第6章/tornado_static/tornado_static_server.py
"""

from tornado.web import Application, StaticFileHandler
from tornado.ioloop import IOLoop
import os

APP_ROOT = os.path.dirname(__file__)

if __name__ == '__main__':
    app = Application([
        (
            r"/static/(.*)",
            StaticFileHandler,
            # 配置当前文件同目录下的 static 目录为静态文件所在目录
            dict(path=os.path.join(APP_ROOT, "static"))
        )
    ])
    # 侦听端口 8888
    app.listen(8888)
    try:
        # 启动
        IOLoop.current().start()
    except KeyboardInterrupt:
        print("Server stopped by user")
