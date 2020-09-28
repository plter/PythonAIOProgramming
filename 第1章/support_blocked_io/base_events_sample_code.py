"""
第1章/base_events_sample_code.py
"""


def run_in_executor(self, executor, func, *args):
    self._check_closed()
    if self._debug:
        self._check_callback(func, 'run_in_executor')
    if executor is None:
        executor = self._default_executor
        if executor is None:
            executor = concurrent.futures.ThreadPoolExecutor()
            self._default_executor = executor
    return futures.wrap_future(
        executor.submit(func, *args), loop=self)
