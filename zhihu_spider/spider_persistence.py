# !-*- encoding=utf-8 -*-
"""
持久化类

spider_persistence.py create by v-zhidu
"""

from __future__ import unicode_literals

import json
import os

from spider_logging import SpiderLogging


class SpiderPersistence(object):
    """
    持久化类
    """

    def __init__(self):
        self._logger = SpiderLogging(SpiderPersistence.__name__).logger

    @staticmethod
    def save_to_file(file_path, data, is_serialize=False):
        """
        保存文件
        """
        directory, file_name = os.path.split(file_path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        if is_serialize:
            with open(os.path.join(directory, file_name), 'w') as f:
                f.writelines(json.dumps(data, ensure_ascii=False))
        else:
            with open(os.path.join(directory, file_name), 'w') as f:
                f.writelines(data)


if __name__ == '__main__':

    d = dict(id=1, name='a', url='#a')

    SpiderPersistence.save_to_file('./data/error.txt', d, True)
