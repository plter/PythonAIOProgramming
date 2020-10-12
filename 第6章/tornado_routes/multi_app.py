"""
第6章/tornado_routes/multi_app.py
"""
import tornado.ioloop
from tornado.web import Application
from tornado.routing import Rule, RuleRouter, PathMatches


class HandlerInApp1(tornado.web.RequestHandler):
    def get(self):
        self.write("Handler in app1")


app1 = Application([
    (r"/app1/handler", HandlerInApp1)
])


class HandlerInApp2(tornado.web.RequestHandler):
    def get(self):
        self.write("Handler in app2")


app2 = Application([
    (r"/app2/handler", HandlerInApp2)
])

if __name__ == '__main__':
    # 创建服务器
    server = tornado.web.HTTPServer(
        RuleRouter([
            Rule(PathMatches(r"/app1.*"), app1),
            Rule(PathMatches(r"/app2.*"), app2)
        ])
    )
    # 侦听端口 8888
    server.listen(8888)
    # 启动
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Server stopped by user")
