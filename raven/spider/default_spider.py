# !-*- encoding=utf-8 -*-
"""
默认爬取器.

default_spider.py create by v-zhidu
"""

from base_spider import BaseSpider


class DefaultSpider(BaseSpider):
    """
    默认爬取器.
    """

    def find_links(self, html):
        """
        筛选链接
        """
        self.raven.filters.filter(html)

    def run(self, url, **kwargs):
        self._logger.info('start spider - ' + __name__)
        self.raven.queue.add_unvisited_url(url)

        while not self.raven.queue.unvisited_url_empty():
            url = self.raven.queue.pop_unvisited_url()
            self._logger.info('get - ' + url)
            html = self.raven.client.get(url).read()
            self.find_links(html)
