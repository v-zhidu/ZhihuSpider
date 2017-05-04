# !-*- encoding=utf-8 -*-
"""
抓取知乎话题数据

crawl_topic.py create by v-zhidu
"""

from __future__ import unicode_literals

import os

import spider_const as SpiderConst
from browser import Browser
from spider_decorators import log_url
from spider_logging import SpiderLogging
from spider_parser import SpiderParser


class CrawlTopic(object):
    """
    Summary of class here.

    Longer class information....

    Public Attributes
         An integer count of the eggs we have laid.
    """

    def __init__(self):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        self._browser = Browser()
        self._logger = SpiderLogging(CrawlTopic.__name__).logger

    @log_url
    def get_root_topics(self, url):
        """获取根节点话题

        Logger method information

        Args:
             None
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        response = self._browser.get(url)

        if response is None:
            self._logger.error('响应数据错误, url: ' + url)
            raise ValueError('Invalid response, url=' + url)

        self._logger.debug('解析数据......')
        root_topics = SpiderParser.find_root_topic(response.read())
        self._logger.info('获取到%s个根节点话题路径', len(root_topics))

        return root_topics

    def get_topic_by_id(self, topic):
        """获取第二级话题

        Logger method information

        Args:
             url: str类型，待获取的二级话题页面
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        # 封装请求参数

        all_topics = []
        for off_set in (x * 20 for x in range(0, 5)):
            print off_set
            response = self._browser.topic_list(topic['id'], off_set)

            if response is None:
                self._logger.error('响应数据错误, topic: ' + topic['name'])
                raise ValueError('Invalid response, topic=' + topic['name'])

            self._logger.debug('查找-%s-话题下所有子话题......', topic['name'])
            result = SpiderParser.find_topic(response.read())

            if len(result) is 0:
                break

            for item in result:
                self._logger.debug('%s -> %s', item['name'], item['url'])
                all_topics.append(item)

        self._logger.info('-%s-话题下有%d子话题......',
                          topic['name'], len(all_topics))
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
            raise ValueError('Invalid response, url=' + topic['url'])

        self._logger.debug('下载数据......')
        data_folder = './data/'
        topic_foler = data_folder + root_topic_name
        data_file = topic['name'] + '.html'

        if not os.path.exists(data_folder):
            os.mkdir(data_folder)

        if not os.path.exists(topic_foler):
            os.mkdir(topic_foler)

        with open(os.path.join(topic_foler, data_file), mode='w') as f:
            f.write(response.read())

    def run(self):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        root_topics = self.get_root_topics(
            SpiderConst.ZHIHU_HOST + SpiderConst.ZHIHU_TOPICS)

        # 遍历查找所有话题路径
        for topic in root_topics:
            data = self.get_topic_by_id(topic)
            for item in data:
                self.download_topic_detail(topic['name'], item)

    @property
    def browser(self):
        """返回http客户端实例.
        """
        return self._browser
