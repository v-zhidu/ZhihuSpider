# !-*- encoding=utf-8 -*-
'''
处理和网络相关的操作模块

browser.py create by v-zhidu
'''

from __future__ import unicode_literals

import logging
import socket
import time
import urllib
import urllib2


class DefaultClient(object):
    """
    处理和网络相关的操作客户端
    """
    default_headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN, zh; q=0.8, en; q=0.6'
    }

    def __init__(self, **kwargs):
        self._headers = kwargs.get('request_headers', self.default_headers)
        self._logger = kwargs.get('logger', logging.getLogger(__name__))

        # 设置全局超时
        timeout = kwargs.get('time_out', 10)
        socket.setdefaulttimeout(timeout)

    @property
    def headers(self):
        """
        返回请求头
        """
        return self._headers

    @headers.setter
    def headers(self, key, value):
        """
        添加请求头
        """
        self._headers[key] = value

    def get(self, url, delay=0):
        """
        Get方式打开链接

        Args:
            url: str类型字符串，指向需要获取的链接地址
        Returns:
            返回html页面数据
        Raises:
            TypeError:
            HttpError:
        """
        try:
            if delay:
                time.sleep(delay)

            self._logger.debug('请求地址 %s', url)
            response = urllib2.urlopen(url, data=None)

            return response
        except urllib2.HTTPError as e:
            self._logger.error(
                'HTTPERROR - code=%s, msg=%s, url=%s', e.code, e.message, url)
        except urllib2.URLError as e:
            self._logger.error(
                'URLError - message=%s url=%s', e.reason, url)

    def post(self, url, data=None, delay=0):
        """
        post请求
        """
        try:
            if delay:
                time.sleep(delay)

            data = urllib.urlencode(data)
            request = urllib2.Request(url, data)
            response = urllib2.urlopen(request)

            return response
        except urllib2.HTTPError as e:
            self._logger.error(
                'HTTPERROR - code=%s, msg=%s, url=%s', e.code, e.message, url)
        except urllib2.URLError as e:
            self._logger.error(
                'URLError - message=%s url=%s', e.reason, url)


if __name__ == '__main__':

    import sys
    sys.path.append('/Users/duzhiqiang/Code/ZhihuSpider/')
