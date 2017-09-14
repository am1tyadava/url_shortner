# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class WebUrl(models.Model):
    url = models.URLField()
    created = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('id',)
