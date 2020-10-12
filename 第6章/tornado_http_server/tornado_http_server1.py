"""
第6章/tornado_http_server/tornado_http_server1.py
"""

import tornado.ioloop
import tornado.web

if __name__ == '__main__':
    # 创建Web服务器应用
    app = tornado.web.Application()
    app.listen(8888)  # 侦听端口 8888
    tornado.ioloop.IOLoop.current().start()  # 启动
