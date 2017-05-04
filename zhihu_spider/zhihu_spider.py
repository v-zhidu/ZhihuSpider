# !-*- encoding=utf-8 -*-
"""
爬虫模块主程序入口

zhihu_spider.py create by v-zhidu
"""
from __future__ import unicode_literals

from crawl_topic import CrawlTopic


class ZhihuSpider(object):
    """
    知乎爬虫函数
    调度函数
    Public Attributes
    """

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
        topic.run_first_page()


if __name__ == '__main__':
    zhihu_spider = ZhihuSpider()

    zhihu_spider.topics()
