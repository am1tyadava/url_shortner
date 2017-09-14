from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import apis

urlpatterns = [
    # Main API
    url(r'shorten-url/', apis.UrlShortnerApi.as_view()),
    url(r'expand-url/', apis.UrlExpanderApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
