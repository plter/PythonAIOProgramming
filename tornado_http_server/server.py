import tornado.ioloop
import tornado.web


# HomePage 是一个继承自 tornado.web.RequestHandler 的类
class HomePage(tornado.web.RequestHandler):
    async def get(self):
        self.write("Hello World")


if __name__ == '__main__':
    # 创建Web服务器应用
    app = tornado.web.Application([
        # 配置一个请求处理器名为 HomePage，并将其映射到网站根路径 “/” 上，
        # 而 HomePage 是一个继承自 tornado.web.RequestHandler 的类
        ("/", HomePage)
    ])
    app.listen(8888)  # 侦听端口 8888
    tornado.ioloop.IOLoop.current().start()  # 启动
