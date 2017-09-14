# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class ShortenUrl(View):
    TEMPLATE_NAME = 'web/shorten_url.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.TEMPLATE_NAME, context)

    def post(self, request, *args, **kwargs):
        url = request.POST.get("url")
        context = {}
        return render(request, self.TEMPLATE_NAME, context)
