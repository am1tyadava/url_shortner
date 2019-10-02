# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.http.response import HttpResponseRedirect

from django.shortcuts import render
from django.views.generic import View
from shortner.url_ly import UrlLy
from shortner.bit_ly import BitLy


# Create your views here.

class ShortenUrlView(View):
    TEMPLATE_NAME = 'web/shorten_url.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request, *args, **kwargs):
        url = request.POST.get("url")
        urlly = UrlLy()
        shorten_url = urlly.short(url)
        # shorten_url = BitLy().short(url)
        context = {
            'shorten_url': shorten_url,
            'url': url
        }
        return render(request, self.TEMPLATE_NAME, context)


class ExpandUrlView(View):
    def get(self, request, encoded_hash, *args, **kwargs):
        encoded_url = settings.DOMAIN_NAME + "/" + encoded_hash
        urlly = UrlLy()
        try:
            main_url = urlly.expand(encoded_url)
            # main_url = BitLy().expand(encoded_url)
            return HttpResponseRedirect(main_url)
        except:
            context = {
                'error': True,
                'encoded_url': encoded_url
            }
            return render(request, 'web/shorten_url.html', context)
