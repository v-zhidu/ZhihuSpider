# !-*- encoding=utf-8 -*-
"""
redis实现队列的功能

spider_queue_redis.py create by v-zhidu
"""

from spider_queue_base import SpiderQueueBase


class SpiderQueueRedis(SpiderQueueBase):
    """
    redis 实现队列服务
    """

    def __init__(self):
        """
        构造函数
        """
        SpiderQueueBase.__init__(self)

    def add_visited_url(self, url):
        pass
