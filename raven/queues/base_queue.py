# !-*- encoding=utf-8 -*-
"""
队列抽象类

记录url的数据结构

每当要访问一个url的时候, 首先在这个数据结构中查找,如果当前的url已经存在则丢弃，
   1. 结果总保存的url不能重复
   2. 能够快速的查找

spider_queue_base.py create by v-zhidu
"""
from abc import abstractmethod
from raven.adpaters import Adpaters


class BaseQueue(Adpaters):
    """
    存储url数据结构抽象类
    """

    @abstractmethod
    def add_visited_url(self, url, **kwargs):
        """
        添加url到已访问过的url中
        """
        raise self.AdapterMethodNotImplementedError()

    @abstractmethod
    def is_visited_url(self, url):
        """
        检查url是否已经访问过
        """
        raise self.AdapterMethodNotImplementedError()

    @abstractmethod
    def remove_visited_url(self, url):
        """
        删除访问过的url
        """
        raise self.AdapterMethodNotImplementedError()

    @abstractmethod
    def add_unvisited_url(self, url):
        """
        添加未访问的url
        """
        raise self.AdapterMethodNotImplementedError()

    @abstractmethod
    def get_unvisited_url_num(self):
        """
        获取未访问的url数量
        """
        raise self.AdapterMethodNotImplementedError()

    def get_visited_url_num(self):
        """
        返回访问的url数目
        """
        raise self.AdapterMethodNotImplementedError()

    @abstractmethod
    def pop_unvisited_url(self):
        """
        返回行首的url
        """
        raise self.AdapterMethodNotImplementedError()

    @abstractmethod
    def unvisited_url_empty(self):
        """
        判断未访问的url队列是否为空
        """
        raise self.AdapterMethodNotImplementedError()
