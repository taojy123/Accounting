# -*- coding: utf-8 -*-

from django.db import models
import datetime


class Account(models.Model):
    name = models.CharField(max_length=255, blank=True , null=True)
    mao = models.CharField(max_length=255, blank=True , null=True)
    pi = models.CharField(max_length=255, blank=True , null=True)
    jing = models.CharField(max_length=255, blank=True , null=True)
    money = models.CharField(max_length=255, blank=True , null=True)
    time = models.DateTimeField(default=datetime.datetime.now(), auto_now=True)
    status = models.CharField(max_length=255, blank=True , null=True, default="未支付")


    @property
    def showtime(self):
        return self.time.strftime("%Y-%m-%d")

