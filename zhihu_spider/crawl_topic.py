# !-*- encoding=utf-8 -*-
"""
The topic of http://www.zhihu.com process module.

crawl_topic.py create by v-zhidu
"""

from __future__ import unicode_literals

from urlparse import urljoin

import spider_const as SpiderConst
from browser import Browser
from spider_decorators import retry
from spider_logging import SpiderLogging
from spider_parser import SpiderParser
from spider_persistence import SpiderPersistence
from topic import Topic

from queue.spider_queue import SpiderQueue


class CrawlTopic(object):
    """
    话题抓取类
    """

    def __init__(self):
        self._browser = Browser()
        self._queue = SpiderQueue()
        self._persistence = SpiderPersistence()
        self._logger = SpiderLogging(CrawlTopic.__name__).logger

    def find_seed_topics(self):
        """获取根节点话题

        认为http://www.zhihu.com/topics下css为zm-topic-cat-item的所有话题为根节点话题，以此为如果找到所有话题

        Args:
             url：str类型，待访问的链接
        Returns:
             root_topic: dict类型，根话题的集合{'id':'', 'name':'', 'url':''}
        Raises:
             ValueError: 响应数据为空
        """
        url = SpiderConst.ZHIHU_TOPICS

        response = self._browser.get(url)

        self._logger.debug('解析数据......')
        seed_topics = SpiderParser.find_seed_topic(response.read())
        self._logger.info('获取到%s个根节点话题', len(seed_topics))

        return seed_topics

    def find_topic_by_id(self, seed_topic):
        """根据根话题id获取所有子话题

        调用知乎话题列表分页接口获取到所有子话题

        Args:
             url: str类型，待获取的二级话题页面
        Returns:
             dict类型，话题的集合{'id':'', 'name':'', 'url':''}
        Raises:
             ValueError: 响应数据为空
        """
        def _off_set_generator(max_count):
            off_set = 0
            while off_set <= max_count:
                yield off_set
                off_set = off_set + 20

        url = urljoin(SpiderConst.ZHIHU_HOST, SpiderConst.ZHIHU_TOPIC_LIST_API)

        @retry(3)
        def _find_topic_offset():
            response = self._browser.topic_list(url, seed_topic.id, off_set)

            if response is None:
                self._logger.error('响应数据错误, topic: %s -> %s',
                                   seed_topic.name, urljoin(SpiderConst.ZHIHU_TOPICS, seed_topic.url))
                self._logger.warn('请求失败, 重试')
                raise ValueError('response is error')
            else:
                return SpiderParser.find_topic(response.read())

        self._logger.debug(
            '%s -> %s', seed_topic.name, SpiderConst.ZHIHU_TOPICS + '#' + seed_topic.name)

        topics = []
        g = _off_set_generator(SpiderConst.TOPIC_OFF_SET_MAX)
        try:
            while True:
                off_set = g.next()
                result = _find_topic_offset()
                size = len(result)

                if size > 0:
                    topics.extend(result)
                    self._logger.info(len(topics))
                else:
                    raise StopIteration()
        except StopIteration:
            for i in topics:
                self._logger.info('id=%s name=%s', i.id, i.name)
            self._logger.info('Done! count=%d', len(topics))

        return topics

    def save_topic_detail(self, file_name, html):
        """
        持久化话题详情数据
        """
        # 文件实现
        path = './data/topics/%s.html' % (file_name)
        self._logger.debug('download file: %s.html', file_name)
        self._persistence.save_to_file(path, html)

    def download_topic_detail(self, url, save_file=False):
        """
        下载话题详情页面
        """
        response = self._browser.get(url)

        if response is None:
            self._logger.error('响应数据错误, url: ' + url)

        # 持久化
        if save_file:
            self.save_topic_detail(
                str(url).split('/')[4], response.read())
        return response.read()

    def run(self):
        """
        Control the process.
        """
        seed_topics = self.find_seed_topics()
        # 遍历查找所有话题路径

        def _find(seed):
            """
            查找子话题并放入到队列中
            """
            self._logger.info('search %s', seed.name)
            topics = self.find_topic_by_id(seed)
            for topic in topics:
                self._queue.add_unvisited_url(
                    urljoin(SpiderConst.ZHIHU_HOST, topic.url))

            return topics

        all_topics = reduce(lambda x, y: x + y, map(_find, seed_topics))
        self._logger.info('topics all count -> %s', len(all_topics))

        print self._queue.get_unvisited_url_num()
        print self._queue.get_visited_url_num()
        # 下载页面
        # while self._queue.unvisited_url_empty():
        #     url_to_do = self._queue.pop_unvisited_url()
        #     self.download_topic_detail(url_to_do, True)
        #     self._queue.add_visited_url(url_to_do)

    @property
    def browser(self):
        """
        返回http客户端实例.
        """
        return self._browser

    @property
    def queue(self):
        """
        返回队列结构
        """
        return self._queue


if __name__ == '__main__':

    c = CrawlTopic()
    c.find_topic_by_id(Topic(395, '投资', '#投资'))
