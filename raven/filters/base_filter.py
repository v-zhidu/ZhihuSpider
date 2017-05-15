# !-*- encoding=utf-8 -*-
"""
筛选器基类

base_filter.py create by v-zhidu
"""

import logging

from abc import abstractmethod


class BaseFilter(object):
    """
    筛选器基类
    """

    def __init__(self, **kwargs):
        self._logger = kwargs.get('logger', logging.getLogger(__name__))

    @abstractmethod
    def filter(self, html):
        """
        筛选方法
        """
        pass
