# !-*- encoding=utf-8 -*-
"""
项目中的所以装饰器

record_decorator.py create by v-zhidu
"""

# from spider_logging import SpiderLogging
# logger = SpiderLogging()

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
