# !-*- encoding=utf-8 -*-
"""
A basic spider-framework.

raven.py create by v-zhidu
"""

from util import initialize_class


class Raven(object):
    """
    Appication Entry

    raven.py create by v-zhidu
    """

    def __init__(self, name, **kwargs):
        self._name = name

        # 加载http模块
        http_client = kwargs.get(
            'http_client', 'raven.http_client.DefaultClient')
        # 单个spider
        spiders = kwargs.get('spiders', 'raven.spider.DefaultSpider')
        # 单个筛选器
        filters = kwargs.get('filters', 'raven.filters.DefaultFilter')
        # 加载队列模块
        queue = kwargs.get('queue', 'raven.queues.BaseQueue')

        # import class
        self._client = initialize_class(http_client, **kwargs)
        self._spiders = initialize_class(spiders, **kwargs)
        self._queue = initialize_class(queue, **kwargs)
        self._filters = initialize_class(filters, **kwargs)

        self._spiders.raven = self

    @property
    def client(self):
        """
        允许外部访问http_client
        """
        return self._client

    @property
    def queue(self):
        """
        允许外部访问队列
        """
        return self._queue

    @property
    def filters(self):
        """
        允许访问筛选器
        """
        return self._filters

    def start(self, url):
        """
        Release the spider.
        """
        self._spiders.run(url)
