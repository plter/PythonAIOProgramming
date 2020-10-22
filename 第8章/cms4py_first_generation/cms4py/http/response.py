"""
第8章/cms4py_first_generation/cms4py/http/response.py
"""

import config
from cms4py.http.request import Request


class Response:
    def __init__(self, request: Request, send):
        self._send = send
        # 该变量用于记录返回的 content_type 类型
        self._content_type = None
        # 该变量用于指示头部是否已发送
        self._header_sent = False
        # 该变量用户指示内容是否已发送
        self._body_sent = False
        self._body = b''
        # 记录Request对象
        self._request: Request = request

        # 返回的头部信息
        self._headers_map = {}

        # 指定默认的 content_type 是 text/html
        self.content_type = b'text/html'
        # 添加自定义的服务器名称信息
        self.add_header(b'server', config.SERVER_NAME)
        pass

    @property
    def header_sent(self):
        return self._header_sent

    def _get_headers(self):
        result = []
        for key in self._headers_map:
            for v in self._headers_map[key]:
                result.append([key, v])
        return result

    def add_header(self, key: bytes, value: bytes):
        if key not in self._headers_map:
            self._headers_map[key] = []
        self._headers_map[key].append(value)

    @property
    def body_sent(self):
        return self._body_sent

    @property
    def content_type(self) -> bytes:
        return self._content_type

    @content_type.setter
    def content_type(self, value: bytes):
        self._content_type = value
        self._headers_map[b"content-type"] = [value]

    @property
    def body(self):
        return self._body

    async def send_header(self, status=200):
        """
        发送协议头
        :param status:
        :return:
        """
        await self._send({
            'type': 'http.response.start',
            'status': status,
            'headers': self._get_headers()
        })
        self._header_sent = True

    async def write(self, data: bytes):
        """
        向浏览器端写数据，但不关闭连接
        :param data:
        :return:
        """
        if not self._header_sent:
            await self.send_header()
        await self._send({
            "type": "http.response.body",
            "body": data,
            # 如果指定 more_body 为 True，则意味着还有待发
            # 数据，连接需要被继续保持
            'more_body': True
        })

    async def end(self, data: bytes):
        """
        该函数用于发送数据之后关闭连接
        :param data:
        :return:
        """
        if self._body_sent:
            return
        if not self._header_sent:
            await self.send_header()
        await self._send({
            "type": "http.response.body",
            "body": data,
            'more_body': False
        })
        self._body = data
        self._body_sent = True
