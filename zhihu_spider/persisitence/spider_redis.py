# !-*- encoding=utf-8 -*-
"""
redis 帮助类

spider_redis.py create by v-zhidu
"""

import redis


class SpiderRedis(object):
    """
    Redis类
    """

    def __init__(self):
        self._client = redis.Redis(host='121.42.244.187', port=3387)

    def set(self, key, value):
        """
        设置值
        """
        self._client.set(key, value)

    def get(self, key):
        """
        取值
        """
        return self._client.get(key)


if __name__ == '__main__':
    re = SpiderRedis()
    # re.set('hello', 'world')
    print re.get('hello')
