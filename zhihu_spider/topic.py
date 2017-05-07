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

    def __init__(self, topic_id, name, url, html=None):
        self._id = topic_id
        self._name = name
        self._url = url
        self._html = html

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

    @property
    def html(self):
        """
        获取话题页面
        """
        return self._html

    @url.setter
    def url(self, value):
        """
        设置话题页面
        """
        self._url = value
