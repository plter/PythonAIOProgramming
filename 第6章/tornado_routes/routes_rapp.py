"""
第6章/tornado_routes/routes_rapp.py
"""
import tornado.ioloop
import tornado.web
import tornado.routing


class AppPage(tornado.web.RequestHandler):
    def get(self, path_arg1, path_arg2):
        """
        该函数必须可以接受两个参数
        :param path_arg1: 对应正则表达式截取的第1个变量
        :param path_arg2: 对应正则表达式截取的第2个变量
        :return:
        """
        self.write(f"Arg1 is: {path_arg1}, arg2 is:{path_arg2}")


if __name__ == '__main__':
    # 创建Web服务器应用
    app = tornado.web.Application([
        # 该路径设置了两个截取的的变量
        (r"/app/(.*)/(.*)", AppPage)
    ])
    app.listen(8888)  # 侦听端口 8888
    tornado.ioloop.IOLoop.current().start()  # 启动
