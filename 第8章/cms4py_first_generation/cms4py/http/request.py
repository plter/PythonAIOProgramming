"""
第8章/cms4py_first_generation/cms4py/http/request.py
"""

import config
import re


class Request:
    """
    将浏览器的请求封装为一个Request对象，便于操作
    """

    def __init__(self, scope, receive):
        self._scope = scope
        self._receive = receive
        # 记录协议类型， http 或者 https
        self._protocol = scope['scheme']
        # 记录请求方法
        self._method = self._scope['method']
        # 记录请求路径
        self._path = self._scope['path']
        # 记录请求路径中 ? 后面的字符串
        self._query_string = self._scope['query_string']
        # 记录 ASGI 发来的原始请求头数据
        self._raw_headers = self._scope['headers'] \
            if 'headers' in self._scope else []
        # 声明一个字典用于存放头数据
        self._headers = {}
        # 将原始请求头数据装进 self._headers，便于后续使用
        self._copy_headers()
        # 记录原始请求头中的可接受的语言列表数据
        self._raw_accept_languages = self.get_header(b'accept-language')
        # 用正则表达将可接受的语言截取出来转成数组
        self._accept_languages = re.compile(b"[a-z]{2}-[A-Z]{2}").findall(
            self._raw_accept_languages
        ) if self._raw_accept_languages else []

        lang: bytes = config.LANGUAGE or (
            self._accept_languages[0] if len(self._accept_languages) > 0 else b'en-US'
        )
        # 记录将要使用的语言种类
        self._language = lang.decode("utf-8")

        # 该变量用于记录 content_type
        self._content_type = None
        # 该变量用于记录请求的 uri
        self._uri = None
        # 记录请求的主机
        self._host = self.get_header(b"host")
        # 记录信息
        self._client = self._scope['client']
        # 记录客户端 ip 地址
        self._client_ip = self._client[0]
        # 记录客户端端口
        self._client_port = self._client[1]

        # 该变量用于记录请求的控制器名
        self._controller = None
        # 该变量用于记录请求的函数名
        self._action = None
        # 该变量用于记录路径参数
        self._args = None
        pass

    @property
    def controller(self):
        return self._controller

    @property
    def action(self):
        return self._action

    @property
    def host(self) -> bytes:
        return self._host

    def host_as_str(self, charset=config.GLOBAL_CHARSET) -> str:
        return self.host.decode(charset) if self.host else ''

    @property
    def client_ip(self):
        return self._client_ip

    @property
    def protocol(self) -> str:
        return self._protocol

    @property
    def uri(self) -> str:
        if not self._uri:
            self._uri = self.path
            if self.query_string:
                self._uri += "?"
                self._uri += self.query_string.decode(
                    config.GLOBAL_CHARSET
                )
        return self._uri

    def _copy_headers(self):
        # 将原始请求头数据装进 self._headers
        # 在 HTTP 协议中，消息头可以支持多条同名的字段，所以字段名
        # 对应的是个列表对象
        for pair in self._raw_headers:
            if len(pair) == 2:
                key = pair[0]
                if key not in self._headers:
                    self._headers[key] = []
                self._headers[key].append(pair[1])
        pass

    @property
    def language(self) -> str:
        return self._language

    @property
    def accept_languages(self):
        return self._accept_languages

    @property
    def headers(self):
        return self._headers

    def is_mobile(self):
        user_agent = self.get_header(b"user-agent")
        if user_agent:
            return user_agent.find(b"iPhone") != -1 or \
                   user_agent.find(b"iPad") != -1 or \
                   user_agent.find(b"Android") != -1
        return False

    @property
    def query_string(self) -> bytes:
        return self._query_string

    def _get_first_value_of_array_map(self, data, key):
        values = data[key] if (data and key in data) else None
        value = None
        if values and len(values) > 0:
            value = values[0]
        return value

    def get_headers(self, key: bytes):
        """
        Get all values by key
        :param key:
        :return:
        """
        return self.headers[key] if key in self.headers else None

    def get_header(self, key: bytes, default_value=None) -> bytes:
        """
        Get first value by key
        :param key:
        :param default_value:
        :return:
        """
        return self._get_first_value_of_array_map(
            self.headers, key
        ) or default_value

    @property
    def content_type(self) -> bytes:
        if not self._content_type:
            self._content_type = self.get_header(b"content-type")
        return self._content_type

    @property
    def method(self) -> str:
        return self._method

    @property
    def path(self) -> str:
        return self._path

    @property
    def args(self):
        """
        获取所有的路径参数
        :return:
        """
        return self._args

    def arg(self, index):
        """
        返回指定位置的值或者 None
        :param index:
        :return:
        """
        return self.args[index] \
            if self.args and len(self.args) > index \
            else None
