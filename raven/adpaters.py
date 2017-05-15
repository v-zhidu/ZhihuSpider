# !-*- encoding=utf-8 -*-
"""
适配器基类

adpaters.py create by v-zhidu
"""

import logging


class Adpaters(object):
    """
    所有适配器类的基类
    """

    def __init__(self, **kwargs):
        self._logger = kwargs.get('logger', logging.getLogger(__name__))
        self._raven = None

    @property
    def raven(self):
        """
        赋予一个适配器类访问raven实例的权限
        """
        return self._raven

    @raven.setter
    def raven(self, raven):
        self._raven = raven

    class AdapterMethodNotImplementedError(NotImplementedError):
        """
        An exception to be raised when an adapter method has not been implemented.
        Typically this indicates that the developer is expected to implement the
        method in a subclass.
        """

        def __init__(self, message=None):
            """
            Set the message for the esception.
            """
            if not message:
                message = 'This method must be overridden in a subclass method.'
            self.message = message

        def __str__(self):
            return self.message
