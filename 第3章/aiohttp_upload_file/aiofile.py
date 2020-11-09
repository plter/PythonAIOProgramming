import asyncio
from typing import Any


class AsyncFunWrapper:

    def __init__(self, blocked_fun) -> None:
        super().__init__()
        self._blocked_fun = blocked_fun

    def __call__(self, *args):
        return asyncio.get_running_loop().run_in_executor(
            None,
            self._blocked_fun,
            *args
        )


class AIOWrapper:
    def __init__(self, blocked_file_io) -> None:
        super().__init__()
        self._blocked_file_io = blocked_file_io

    def __getattribute__(self, name: str) -> Any:
        return AsyncFunWrapper(
            super().__getattribute__("_blocked_file_io").__getattribute__(name)
        )


async def open_async(*args):
    return AIOWrapper(
        await asyncio.get_running_loop().run_in_executor(None, open, *args)
    )
