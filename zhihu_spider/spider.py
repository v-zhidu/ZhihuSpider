# !-*- encoding=utf-8 -*-
"""
爬虫模块主程序入口

zhihu_spider.py create by v-zhidu
"""
from __future__ import unicode_literals

from crawl_topic import CrawlTopic
from spider_logging import SpiderLogging


class ZhihuSpider(object):
    """
    知乎爬虫函数
    调度函数
    Public Attributes
    """

    def __init__(self):
        self._logger = SpiderLogging(ZhihuSpider.__name__).logger

    @property
    def logger(self):
        """返回logger实例
        """
        return self._logger

    def topics(self):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        topic = CrawlTopic()

        zhihu_spider.logger.info('开始抓取知乎话题数据')
        topic.run()


if __name__ == '__main__':
    zhihu_spider = ZhihuSpider()

    zhihu_spider.topics()
    zhihu_spider.logger.info('成功')
