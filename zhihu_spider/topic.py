# !-*- encoding=utf-8 -*-
"""
topic 类型

topic.py create by v-zhidu
"""

from __future__ import unicode_literals


class Topic(object):
    """
    topic类型
    """
    __slots__ = ('_id', '_name', '_url', '_html')

    def __init__(self, topic_id, name, url):
        self._id = topic_id
        self._name = name
        self._url = url

    def __str__(self):
        return u'topic: %s -> %s -> %s' % (self._id, self._name, self._url)

    @property
    def id(self):
        """
        获取话题id
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        设置话题id
        """
        self._id = value

    @property
    def name(self):
        """
        获取话题名称
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        设置话题名称
        """
        self._name = value

    @property
    def url(self):
        """
        获取话题地址
        """
        return self._url

    @url.setter
    def url(self, value):
        """
        设置话题地址
        """
        self._url = value

    @staticmethod
    def topic_to_json(topic):
        """
        对象序列化方法
        """
        return {
            'id': topic.id,
            'name': topic.name,
            'url': topic.url
        }
