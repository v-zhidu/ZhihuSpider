# !-*- encoding=utf-8 -*-
"""
Zhihu-Spider Module.

Find topic information from zhihu.com

zhihu_spider.py create by v-zhidu
"""
from __future__ import unicode_literals

from crawl_topic import CrawlTopic
from spider_logging import SpiderLogging


class ZhihuSpider(object):
    """
    Application Entry
    """

    def __init__(self):
        self._logger = SpiderLogging(ZhihuSpider.__name__).logger

    def topics(self):
        """
        Get all topics.
        """
        topic = CrawlTopic()

        self._logger.info('Release spider!!!')
        topic.run()
        self._logger.info('Done!')


if __name__ == '__main__':
    zhihu_spider = ZhihuSpider()

    zhihu_spider.topics()
