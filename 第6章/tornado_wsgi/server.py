"""
第6章/tornado_wsgi/server.py
"""

import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
import web2py.wsgihandler

# 创建一个WSGI容器用于支持WSGI应用
wsgi_container = tornado.wsgi.WSGIContainer(
    web2py.wsgihandler.application
)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(
        wsgi_container
    )
    http_server.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("User stopped server")
