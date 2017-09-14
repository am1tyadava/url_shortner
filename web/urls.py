from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShortenUrlView.as_view(), name="shorten_url"),
    url(r'^(?P<encoded_hash>[0-9a-zA-Z]+)$', views.ExpandUrlView.as_view(), name="expand_url"),
]
