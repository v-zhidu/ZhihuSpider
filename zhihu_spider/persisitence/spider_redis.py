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

    def sadd(self, name, value):
        """
        存为集合
        """
        return self._client.sadd(name, value)

    def sismember(self, name, value):
        """
        检查一个元素是否在集合中
        """
        return self._client.sismember(name, value)

    def srem(self, name, value):
        """
        移除集合中的元素，返回移除的元素数量
        """
        return self._client.srem(name, value)

    def scard(self, name):
        """
        返回元素数量
        """
        return self._client.scard(name)

    def hset(self, hash_key, sub_key, value):
        """
        存为散列
        """
        return self._client.hset(hash_key, sub_key, value)


if __name__ == '__main__':
    re = SpiderRedis()
    # re.set('hello', 'world')
    a = 'queue:unvisited'
    print re.rpush(a, '2')
    print re.lrange(a, 0, -1)
