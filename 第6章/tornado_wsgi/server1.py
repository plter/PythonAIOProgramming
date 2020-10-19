"""
第6章/tornado_wsgi/server1.py
"""

import tornado.ioloop
import tornado.web
import tornado.wsgi

import web2py.wsgihandler


class Home(tornado.web.RequestHandler):
    def get(self):
        self.write("Home page")


# 创建一个WSGI容器用于支持WSGI应用
wsgi_container = tornado.wsgi.WSGIContainer(
    web2py.wsgihandler.application
)

if __name__ == '__main__':
    http_server = tornado.web.Application([
        (r"/", Home),
        (
            r"/welcome.*",
            # 使用 FallbackHandler 可将指定的请求交由 wsgi 应用处理
            tornado.web.FallbackHandler,
            dict(fallback=wsgi_container)
        )
    ])
    http_server.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("User stopped server")
