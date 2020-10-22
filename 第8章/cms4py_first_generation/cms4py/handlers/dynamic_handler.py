"""
第8章/cms4py_first_generation/cms4py/handlers/dynamic_handler.py
"""

import config
import os, inspect
import importlib.util
from cms4py.utils import aiofile
from cms4py import http


async def handle_dynamic_request(scope, receive, send) -> bool:
    data_sent = False
    request_path: str = scope['path']

    # 将请求路径分拆为 controller 和 action，例如：/user/list_all 请求
    # 对应的 controller 是 user， action 是 list_all
    tokens = request_path.split("/")
    tokens_len = len(tokens)
    # 指定默认的控制器名
    controller_name = config.DEFAULT_CONTROLLER
    if tokens_len >= 2:
        controller_name = tokens[1] or config.DEFAULT_CONTROLLER
    # 指定默认的函数名
    action_name = config.DEFAULT_ACTION
    if tokens_len >= 3:
        action_name = tokens[2] or config.DEFAULT_ACTION
    controller_file = os.path.join(
        config.CONTROLLERS_ROOT, f"{controller_name}.py"
    )

    controller_object = None
    # 如果文件存在，尝试将该文件导入为模块
    if await aiofile.exists(controller_file):
        # 根据浏览器请求路径导入指定的模块
        controller_object = importlib.import_module(
            f"{config.APP_DIR_NAME}.{config.CONTROLLERS_DIR_NAME}.{controller_name}"
        )
        pass

    if controller_object:
        # 根据 action_name 获取指定的成员
        action = getattr(controller_object, action_name, None)
        if action:
            # 构造 HTTP 请求对象，便于后续操作
            req = http.Request(scope, receive)
            # 构造 HTTP 响应对象，便于后续操作
            res = http.Response(req, send)
            req._controller = controller_name
            req._action = action_name
            # 如果 action 是类定义，则先将类实例化再执行
            if inspect.isclass(action):
                await action()(req, res)
            # 否则把 action 当作函数对待直接执行
            else:
                await action(req, res)
            data_sent = res.body_sent
    return data_sent
