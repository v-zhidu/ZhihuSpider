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

    def rpush(self, name, value):
        """
        推送到列表

        返回当前list的大小
        """
        return self._client.rpush(name, value)

    def lpop(self, name):
        """
        从列表左端推出一个元素
        """
        return self._client.lpop(name)

    def lrange(self, name, start, end):
        """
        从列表返回指定范围的元素
        """
        return self._client.lrange(name, start, end)

    def llen(self, name):
        """
        返回列表长度
        """
        return self._client.llen(name)


if __name__ == '__main__':
    re = SpiderRedis()
    # re.set('hello', 'world')
    a = 'queue:unvisited'
    print re.rpush(a, '2')
    print re.lrange(a, 0, -1)
