#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class service_info(models.Model):

    sn = models.CharField(max_length=20)
    name = models.CharField(max_length=255,default='')
    l2tp = models.CharField(max_length=255,default='')
    ssl = models.CharField(max_length=255,default='')
    re = models.CharField(max_length=1000,default='')

class Blog_settings(models.Model):
    Aki = models.CharField(max_length=50,default='')
    Aks = models.CharField(max_length=50,default='')
    Domain_name = models.CharField(max_length=50,default='')
    server = models.CharField(max_length=255,default='')

# Create your models here.
