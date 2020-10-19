"""
第6章/tornado_internationalization/server.py
"""
import tornado.ioloop
import tornado.web
import tornado.locale
import os

SERVER_ROOT = os.path.dirname(__file__)


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        # 根据 url 中的参数 lang 来确定页面语言
        # self.locale = tornado.locale.get(
        #     self.get_query_argument("lang", "en_US")
        # )
        # 渲染模板，并向其传入参数 greeting_word
        await self.render("main.html", greeting_word="Hello")


if __name__ == "__main__":
    # 从指定的目录中加载语言表
    tornado.locale.load_translations(os.path.join(SERVER_ROOT, "languages"))
    application = tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
        # 配置模板文件目录
        template_path=os.path.join(SERVER_ROOT, "template")
    )
    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("User stopped server")
