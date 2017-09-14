# coding: utf-8

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def is_valid_url(url):
    val = URLValidator()
    try:
        val(url)
    except ValidationError:
        return False
    else:
        return True
