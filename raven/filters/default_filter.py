# !-*- encoding=utf-8 -*-
"""
找到所有url

default_filter.py create by v-zhidu
"""

from bs4 import BeautifulSoup

from .base_filter import BaseFilter


class DefaultFilter(BaseFilter):
    """
    默认筛选器，找到所有链接
    """

    def filter(self, html):
        soup = BeautifulSoup(html, 'lxml')
        links = soup.find_all('a', href=True)
        for link in links:
            self._logger.debug(link)
