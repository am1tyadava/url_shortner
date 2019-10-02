# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class WebUrl(models.Model):
    url = models.URLField()
    created = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return "Url - {0} created on {1} with id: {2}".format(self.url, self.created, self.id)

    class Meta:
        ordering = ('id',)
