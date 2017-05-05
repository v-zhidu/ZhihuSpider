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


class CrawlTopic(object):
    """
    Crawl Topic Class.
    """

    def __init__(self):
        self._browser = Browser()
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

        if response is None:
            self._logger.error('响应数据错误, url: ' + url)
            raise ValueError('Invalid response, url=' + url)

        self._logger.debug('解析数据......')
        root_topics = SpiderParser.find_seed_topic(response.read())
        self._logger.info('获取到%s个根节点话题', len(root_topics))

        return root_topics

    def get_topic_by_id(self, seed_topic):
        """根据根话题id获取所有子话题

        调用知乎话题列表分页接口获取到所有子话题

        Args:
             url: str类型，待获取的二级话题页面
        Returns:
             dict类型，话题的集合{'id':'', 'name':'', 'url':''}
        Raises:
             ValueError: 响应数据为空
        """
        all_topics = []
        failed_requests = []

        def _get_topic_by_id(off_set):
            try:
                return _get_topic_offset(off_set)
            except ValueError as ex:
                failed_requests.append(
                    dict(id=seed_topic['id'], name=seed_topic['name'], off_set=off_set, err_msg=ex.message))

        def _get_topic_offset(off_set):
            response = self._browser.topic_list(seed_topic['id'], off_set)

            if response is None:
                self._logger.error('响应数据错误, topic: ' + seed_topic['name'])
                raise ValueError('响应数据错误, topic: ' + seed_topic['name'])
            else:
                return SpiderParser.find_topic(response.read())

        self._logger.debug(
            '%s -> %s', seed_topic['name'], SpiderConst.ZHIHU_TOPICS + seed_topic['url'])

        for off_set in (x * 20 for x in range(1, 100)):
            result = _get_topic_by_id(off_set)

            if len(result) is 0:
                self._logger.info('Done! count=%d', len(all_topics))
                break
            else:
                self._logger.debug(off_set)
                map(all_topics.append, result)

        self._persistence.save_failed_request(failed_requests)
        return all_topics

    def download_topic_detail(self, root_topic_name, topic):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        response = self._browser.get(SpiderConst.ZHIHU_HOST + topic['url'])

        if response is None:
            self._logger.error('响应数据错误, url: ' + topic['url'])

        self._persistence.save_topic_detail(
            root_topic_name, topic, response.read())

    def find_topic_detail_and_download(self, seed_topic):
        """
        search all topic by a seed topic.
        """
        self._logger.info('search %s', seed_topic['name'])
        data = self.get_topic_by_id(seed_topic)
        for item in data:
            self.download_topic_detail(seed_topic['name'], item)
        self._logger.info('%s have %d child topic',
                          seed_topic['name'], len(data))

    def run(self):
        """
        Control the process.
        """
        seed_topics = self.get_seed_topics(
            SpiderConst.ZHIHU_HOST + SpiderConst.ZHIHU_TOPICS)

        # 遍历查找所有话题路径
        map(self.find_topic_detail_and_download, seed_topics)

    @property
    def browser(self):
        """
        返回http客户端实例.
        """
        return self._browser


if __name__ == '__main__':

    c = CrawlTopic()

    map(c.find_topic_detail_and_download, [
        {'id': '253', 'name': '游戏', 'url': '#游戏'}])
