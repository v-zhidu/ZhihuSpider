# !-*- encoding=utf-8 -*-
'''
处理和网络相关的操作模块

browser.py create by v-zhidu
'''

import time
import urllib2


class Browser(object):
    """
    Summary of class here.

    Longer class information....

    Public Attributes
         An integer count of the eggs we have laid.
    """

    def __init__(self):
        self.__headers__ = {
            'Host': 'www.zhihu.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN, zh; q=0.8, en; q=0.6'
        }

    @property
    def header(self):
        '''Summary of method here.

        Logger method information

        Args:
             An integer list.
        Returns:
             The sum of an integer list.
        Raises:
             The input args must be int type.
        '''
        return self.__headers__

    def get(self, url, delay=0, timeout=10):
        """Get方式打开链接

        通过Get方式打开链接，无登陆验证

        Args:
            url: str类型字符串，指向需要获取的链接地址
        Returns:
            返回html页面数据
        Raises:
            TypeError:
            HttpError:
        """
        if delay:
            time.sleep(delay)
        # request = urllib2.Request(url, data=None, headers=self.__headers__)
        response = urllib2.urlopen(url, data=None, timeout=timeout)

        return response
