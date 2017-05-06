# !-*- encoding=utf-8 -*-
"""
The topic of http://www.zhihu.com process module.

crawl_topic.py create by v-zhidu
"""

from __future__ import unicode_literals

import spider_const as SpiderConst
from browser import Browser
from spider_decorators import log_url
from spider_logging import SpiderLogging
from spider_parser import SpiderParser
from spider_persistence import SpiderPersistence
from spider_queue import SpiderQueue


class CrawlTopic(object):
    """
    话题抓取类
    """

    def __init__(self):
        self._browser = Browser()
        self._queue = SpiderQueue()
        self._persistence = SpiderPersistence()
        self._logger = SpiderLogging(CrawlTopic.__name__).logger

    @log_url
    def get_seed_topics(self, url):
        """获取根节点话题

        认为http://www.zhihu.com/topics下css为zm-topic-cat-item的所有话题为根节点话题，以此为如果找到所有话题

        Args:
             url：str类型，待访问的链接
        Returns:
             root_topic: dict类型，根话题的集合{'id':'', 'name':'', 'url':''}
        Raises:
             ValueError: 响应数据为空
        """
        response = self._browser.get(url)

        self._logger.debug('解析数据......')
        seed_topics = SpiderParser.find_seed_topic(response.read())
        self._logger.info('获取到%s个根节点话题', len(seed_topics))

        return seed_topics

    def get_topic_by_id(self, seed_topic_id, seed_topic_name):
        """根据根话题id获取所有子话题

        调用知乎话题列表分页接口获取到所有子话题

        Args:
             url: str类型，待获取的二级话题页面
        Returns:
             dict类型，话题的集合{'id':'', 'name':'', 'url':''}
        Raises:
             ValueError: 响应数据为空
        """
        url = SpiderConst.ZHIHU_TOPIC_LIST_API

        all_topics = {}

        def _off_set_generator(max_count):
            off_set = 20
            while off_set <= max_count:
                yield off_set
                off_set = off_set + 20

        def _get_topic_offset(off_set):
            response = self._browser.topic_list(url, seed_topic_id, off_set)

            if response is None:
                self._logger.error('响应数据错误, topic: ' + seed_topic_name)
                # TODO(du_zhi_qiang@163.com): 失败后处理
            else:
                return SpiderParser.find_topic(response.read())

        self._logger.debug(
            '%s -> %s', seed_topic_name, SpiderConst.ZHIHU_TOPICS + '#' + seed_topic_name)

        g = _off_set_generator(SpiderConst.TOPIC_OFF_SET_MAX)
        try:
            while True:
                off_set = g.next()
                result = _get_topic_offset(off_set)

                if len(result) is 0:
                    raise StopIteration()
                else:
                    self._logger.debug(off_set)
                    all_topics = dict(all_topics.items() + result.items())
        except StopIteration:
            self._logger.info('Done! count=%d', len(all_topics))

        return all_topics

    def download_topic_detail(self, url):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        response = self._browser.get(url)

        if response is None:
            self._logger.error('响应数据错误, url: ' + url)

        self._persistence.save_topic_detail(
            str(url).split('/')[4], response.read())

    def push_topic_detail_url(self, seed_topic_id, seed_topic_name):
        """
        search all topic by a seed topic.
        """
        self._logger.info('search %s', seed_topic_name)
        data = self.get_topic_by_id(seed_topic_id, seed_topic_name)
        for item in data.itervalues():
            self._queue.add_unvisited_url(SpiderConst.ZHIHU_HOST + item['url'])

    def run(self):
        """
        Control the process.
        """
        seed_topics = self.get_seed_topics(SpiderConst.ZHIHU_TOPICS)
        # 遍历查找所有话题路径
        for seed_id, seed in seed_topics.items():
            self.push_topic_detail_url(seed_id, seed['name'])

        # 下载页面
        # while unvisited_url_empty
        #     url_to_do = self._queue.pop_unvisited_url()
        #     self.download_topic_detail(url_to_do)
        #     self._queue.add_visited_url(url_to_do)

    @property
    def browser(self):
        """
        返回http客户端实例.
        """
        return self._browser


if __name__ == '__main__':

    c = CrawlTopic()

    a = c.get_seed_topics(SpiderConst.ZHIHU_TOPICS)
