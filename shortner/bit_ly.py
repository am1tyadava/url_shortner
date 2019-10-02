from shortner.exceptions import ShorteningException, ExpandingException
from .base_shortner import BaseShortener


class BitLy(BaseShortener):
    api_url = "https://bitly.com"

    def __init__(self, **kwargs):
        kwargs['timeout'] = (3.0, 27)
        super(BitLy, self).__init__(**kwargs)

    def short(self, url):
        shorten_url = self.api_url + "/data/shorten"
        data = {
            'url': url
        }
        # TODO - Some kind of authentication system needs to be added
        # TODO - Need to pass some headers also here
        headers = {}
        response = self._post(shorten_url, data=data, headers=headers)
        if response.ok:
            return response.json().get("data").get("anon_shorten").get("link")
        raise ShorteningException(
            'An error occurred while shortening url - %s' % url
        )

    def expand(self, url):
        """
        No need to implement this as this would be done by bit.ly
        :param url:
        :return:
        """
        return url
