# !-*- encoding=utf-8 -*-
"""
默认爬取器

default_spider.py create by v-zhidu
"""

from abc import abstractmethod

from raven.adpaters import Adpaters


class BaseSpider(Adpaters):
    """
    爬取器基类

    default_spider.py create by v-zhidu
    """

    @abstractmethod
    def run(self, **kwargs):
        """
        运行爬取器
        """
        raise self.AdapterMethodNotImplementedError()
