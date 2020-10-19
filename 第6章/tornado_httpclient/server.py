"""
第6章/tornado_httpclient/server.py
"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 获取 get 方式传来的参数
        name = self.get_query_argument("name", "")
        self.write(f"Hello {name}")

    def post(self):
        # 获取 post 方式传来的参数
        name = self.get_body_argument("name", "")
        self.write(f"Hello {name}")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("User stopped server")
