# !-*- encoding=utf-8 -*-
"""
A basic spider-framework.

raven.py create by v-zhidu
"""

from util import initialize_class


class Raven(object):
    """
    Appication Entry

    raven.py create by v-zhidu
    """

    def __init__(self, name, **kwargs):
        self._name = name
        http_client = kwargs.get(
            'http_client', 'raven.http_client.DefaultClient')

        # import class
        self._client = initialize_class(http_client, **kwargs)

        print self._client.get('http://www.baidu.com')
