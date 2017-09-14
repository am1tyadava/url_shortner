# coding: utf-8
from __future__ import unicode_literals


class UnknownShortenerException(Exception):
    pass


class ShorteningException(Exception):
    pass


class ExpandingException(Exception):
    pass
