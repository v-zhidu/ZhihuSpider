# !-*- encoding=utf-8 -*-
"""
默认爬取器

default_spider.py create by v-zhidu
"""

from raven.spider import BaseSpider


class DefaultSpider(BaseSpider):
    """
    默认爬取器

    default_spider.py create by v-zhidu
    """

    def run(self):
        self._logger.info(__name__)
