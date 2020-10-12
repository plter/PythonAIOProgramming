"""
第6章/tornado_routes/routes.py
"""
import tornado.ioloop
import tornado.web
import tornado.routing


# HomePage 是一个继承自 tornado.web.RequestHandler 的类
class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.write("Home")


class Users(tornado.web.RequestHandler):
    def get(self):
        self.write("Users")


class AppPage(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Request path is: {self.request.path}")


if __name__ == '__main__':
    # 创建Web服务器应用
    app = tornado.web.Application([
        ("/", HomePage),  # 将HomePage映射到 / 路径上
        ("/user", Users),  # 将Users映射到 /users 路径上
        (r"/app.*", AppPage)
    ])
    app.listen(8888)  # 侦听端口 8888
    tornado.ioloop.IOLoop.current().start()  # 启动
