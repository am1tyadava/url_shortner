from django.conf import settings

from base_shortner import BaseShortener
from shortner.exceptions import ShorteningException, ExpandingException


class UrlLy(BaseShortener):
    api_url = settings.DOMAIN_NAME + "/api/v1"

    def __init__(self, **kwargs):
        kwargs['timeout'] = (3.0, 27)
        super(UrlLy, self).__init__(**kwargs)

    def short(self, url):
        shorten_url = self.api_url + "/shorten-url/"
        data = {
            'url': url
        }
        response = self._post(shorten_url, data=data)
        if response.ok:
            return response.json().get("shorten_url")
        raise ShorteningException(
            'An error occurred while shortening url - %s' % url
        )

    def expand(self, url):
        expand_url = self.api_url + "/expand-url/"
        data = {
            'url': url
        }
        response = self._post(expand_url, data=data)
        if response.ok:
            return response.json().get("url")
        raise ExpandingException(
            'An error occurred while expanding url - %s' % url
        )
