# !-*- encoding=utf-8 -*-
"""
知乎内容解析类，包含不同页面的解析方法

content_parser.py create by v-zhidu
"""

from __future__ import unicode_literals

import json

from bs4 import BeautifulSoup

from spider_logging import SpiderLogging

logger = SpiderLogging('ContentParser').logger


class SpiderParser(object):
    """
    知乎内容解析类

    """

    @staticmethod
    def find_seed_topic(html):
        """
        根节点目录的解析方法，在topics页获取所有父级话题以及链接
        """
        logger.debug('查找所有根话题...')
        soup = BeautifulSoup(html, 'lxml')

        topics = {}
        for tag in soup.find_all('li', class_='zm-topic-cat-item'):
            seed_id = tag['data-id']
            topics[seed_id] = dict(
                name=tag.contents[0].string, url=tag.contents[0]['href'])

        return topics

    @staticmethod
    def find_topic(json_data):
        """
        查找二级话题的解析方法，查找所有话题的链接
        """
        result = json.loads(json_data)

        if result is None:
            raise ValueError('json数据为空')

        return SpiderParser.process_topic_list(''.join(result['msg']))

    @staticmethod
    def process_topic_list(html):
        """Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        """
        soup = BeautifulSoup(html, 'lxml')

        topics = {}
        for item in soup.find_all('div', class_='blk'):

            topic_id = item.a['href'][-8:]
            topics[topic_id] = dict(
                name=item.a.strong.string, url=item.a['href'])
        return topics
