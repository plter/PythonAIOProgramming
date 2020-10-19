"""
第6章/tornado_internationalization/server.py
"""
import tornado.ioloop
import tornado.web
import tornado.locale
import os

SERVER_ROOT = os.path.dirname(__file__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 根据浏览器语言自动翻译
        words = self.locale.translate("Hello")
        self.write(f"{words}")


if __name__ == "__main__":
    # 从指定的目录中加载语言表
    tornado.locale.load_translations(os.path.join(SERVER_ROOT, "languages"))
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("User stopped server")
