# !-*- encoding=utf-8 -*-
"""
知乎数据抓取父类

crawl_base.py create by v-zhidu
"""

from __future__ import unicode_literals


class CrawlBase(object):
    """
    定义抓取器共有的一些属性和方法.

    Longer class information....

    Public Attributes
         An integer count of the eggs we have laid.
    """

    def __init__(self):
        self.__host = 'http://www.zhihu.com'

    @property
    def host(self):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        return self.__host
