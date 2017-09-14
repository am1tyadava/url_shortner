from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ShortenUrl.as_view(), name="shorten_url"),
]
