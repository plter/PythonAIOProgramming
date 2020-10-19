"""
第6章/tornado_template/server1.py
"""

import tornado.ioloop
import tornado.web
import os

SERVER_ROOT = os.path.dirname(__file__)


class IndexHandler(tornado.web.RequestHandler):
    async def get(self):
        await self.render("index.html")


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", IndexHandler),
    ], template_path=os.path.join(SERVER_ROOT, "template"))
    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt as e:
        print("User stopped the server")
