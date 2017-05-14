# !-*- encoding=utf-8 -*-
"""
redis实现队列的功能

spider_queue_redis.py create by v-zhidu
"""

import spider_const
from persisitence import SpiderRedis
from spider_queue_base import SpiderQueueBase


class SpiderQueueRedis(SpiderQueueBase):
    """
    redis 实现队列服务
    """

    def __init__(self):
        """
        构造函数
        """
        self._redis = SpiderRedis()

        SpiderQueueBase.__init__(self)

    def add_visited_url(self, url):
        self._redis.sadd(spider_const.TOPICS_SET_VISITED, url)

    def is_visited_url(self, url):
        """
        检查url是否已经访问过
        """
        return self._redis.sismember(spider_const.TOPICS_SET_VISITED, url)

    def remove_visited_url(self, url):
        """
        删除访问过的url
        """
        return self._redis.srem(spider_const.TOPICS_SET_VISITED, url)

    def add_unvisited_url(self, url):
        """
        添加未访问的url
        """
        if not self.is_visited_url(url):
            return self._redis.rpush(spider_const.TOPICS_QUEUE_UNVISITED, url)
        else:
            return self._redis.llen(spider_const.TOPICS_QUEUE_UNVISITED)

    def get_unvisited_url_num(self):
        """
        获取未访问的url数量
        """
        return self._redis.llen(spider_const.TOPICS_QUEUE_UNVISITED)

    def get_visited_url_num(self):
        """
        返回访问的url数目
        """
        return self._redis.scard(spider_const.TOPICS_SET_VISITED)

    def pop_unvisited_url(self):
        """
        返回行首的url
        """
        return self._redis.lpop(spider_const.TOPICS_QUEUE_UNVISITED)

    def unvisited_url_empty(self):
        """
        判断未访问的url队列是否为空
        """
        return self._redis.llen(spider_const.TOPICS_QUEUE_UNVISITED) == 0
