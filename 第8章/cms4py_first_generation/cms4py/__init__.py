"""
第8章/cms4py_first_generation/cms4py/__init__.py
"""

from cms4py.handlers import lifespan_handler
from cms4py.handlers import error_pages
from cms4py.utils.log import Cms4pyLog
from cms4py.handlers import static_file_handler


async def application(scope, receive, send):
    # 获取请求类型
    request_type = scope['type']

    # 如果是 http 类型的请求，则由该程序段处理
    if request_type == 'http':
        data_sent = await static_file_handler.handle_static_file_request(
            scope, send
        )

        # 如果静态文件处理程序未发送数据，则意味着文件找不到，此时应该
        # 向浏览器发送404页面
        if not data_sent:
            # 对于未被处理的请求，均向浏览器发回 404 错误
            await error_pages.send_404_error(scope, receive, send)

    # 如果是生命周期类型的请求，则由该程序段处理
    elif request_type == 'lifespan':
        await lifespan_handler.handle_lifespan(scope, receive, send)
    else:
        Cms4pyLog.get_instance().warning("Unsupported ASGI type")
