# !-*- encoding=utf-8 -*-
"""
抓取知乎话题数据

crawl_topic.py create by v-zhidu
"""

from crawl_base import CrawlBase
from request_client import Browser


class CrawlTopic(CrawlBase):
    """
    Summary of class here.

    Longer class information....

    Public Attributes
         An integer count of the eggs we have laid.
    """

    def __init__(self):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        CrawlBase.__init__(self)

    def run_first_page(self):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        browser = Browser()
        response = browser.get(self.host + '/topics')

        # TODO(du_zhi_qiang@163.com): 分析第一个页面，拿到下一步需要请求的链接

        # TODO(du_zhi_qiang@163.com): 存储页面数据，后续分析数据使用

        print response.read()
