# encoding: utf-8
import requests
from abc import ABCMeta, abstractmethod

from .exceptions import ExpandingException


class BaseShortener(object):
    """
    Base class for all shorteners
    """

    __metaclass__ = ABCMeta

    api_url = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def _post(self, url, data=None, params=None, headers=None):
        response = requests.post(
            url, data=data, params=params,
            headers=headers,
            timeout=self.kwargs['timeout']
        )
        return response

    @abstractmethod
    def short(self, url):
        raise NotImplementedError

    def expand(self, url):
        response = self._get(url)
        if response.ok:
            return response.url
        raise ExpandingException('There was an error expanding this url - {0}'.format(response.content))

    @classmethod
    def __subclasshook__(cls, C):
        if cls is BaseShortener:
            if all(hasattr(C, name) for name in ('short', 'expand')):
                return True
        return NotImplemented
