# !-*- encoding=utf-8 -*-
"""
记录url的数据结构, 内存中的实现方法

spider_queue.py create by v-zhidu
"""

from collections import deque

from spider_queue_base import SpiderQueueBase


class SpiderQueue(SpiderQueueBase):
    """
    存储url的数据结构

    Public Attributes

    visited_url set类型，存储已经访问的url
    unvisited_url deque类型，存储未访问的url
    """

    def __init__(self):
        # 已经访问的url集合
        self._visited_url = set()
        # 未访问的url集合
        self._unvisited_url = deque()

        SpiderQueueBase.__init__(self)

    @property
    def visited_url(self):
        """
        访问已经访问过的url
        """
        # 返回已经访问过的url
        return self._visited_url

    @property
    def unvisited_url(self):
        """
        访问未访问过的url
        """
        # 返回未访问过的url
        return self._unvisited_url

    def add_visited_url(self, url):
        """
        添加url到已访问过的url中
        """
        self._visited_url.add(url)

    def is_visited_url(self, url):
        """
        检查url是否已经访问过
        """
        return url in self.visited_url

    def remove_visited_url(self, url):
        """
        删除访问过的url
        """
        self.visited_url.remove(url)

    def add_unvisited_url(self, url):
        """
        添加未访问的url
        """
        if not isinstance(url, str):
            raise TypeError('url is not a str type.')

        if str(url) is not None and str(url) is not '' and self.is_visited_url(url) is False:
            self._logger.debug('add url into unvisited: %s', url)
            self._unvisited_url.append(url)

    def get_unvisited_url_num(self):
        """
        返回未访问的url数目
        """
        return len(self._unvisited_url)

    def get_visited_url_num(self):
        """
        返回访问的url数目
        """
        return len(self._visited_url)

    def pop_unvisited_url(self):
        """
        返回行首的url
        """
        return self.unvisited_url.pop()

    def unvisited_url_empty(self):
        """
        判断未访问的url队列是否为空
        """
        return len(self._unvisited_url) == 0
