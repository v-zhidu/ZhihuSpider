# !-*- encoding=utf-8 -*-
"""
项目中的所以装饰器

record_decorator.py create by v-zhidu
"""

from __future__ import unicode_literals

from spider_logging import SpiderLogging


logger = SpiderLogging(SpiderLogging.__name__).logger


def log_url(func):
    """
    记录抓取过的页面
    """
    def _log_url(*args, **kwargs):
        """
        打印日志
        """
        logger.info('Get - ' + args[1])

        return func(*args, **kwargs)
    return _log_url


def retry(times=1, exceptions=None):
    exceptions = exceptions if exceptions is not None else Exception

    def wrapper(func):
        def wrapper(*args, **kwargs):
            last_exception = Exception
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
            logger.info('请求失败, 错误原因 - ' + last_exception.message)
            raise last_exception
        return wrapper
    return wrapper
