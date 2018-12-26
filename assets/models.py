#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class service_info(models.Model):

    hostname = models.CharField(max_length=20)
    abroad = models.CharField(max_length=255,default='')
    within = models.CharField(max_length=255,default='')
    diskinfo = models.CharField(max_length=255,default='')
    service_port = models.CharField(max_length=1000,default='')
    cpuinfo = models.CharField(max_length=20,default='')
    meminfo = models.CharField(max_length=20,default='')
    remark = models.CharField(max_length=255,default='')

class Domain_info(models.Model):
    Type = models.CharField(max_length=20)
    Host = models.CharField(max_length=50)
    Value = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)


class Blog_settings(models.Model):
    Aki = models.CharField(max_length=50,default='')
    Aks = models.CharField(max_length=50,default='')
    Domain_name = models.CharField(max_length=50,default='')
    server = models.CharField(max_length=255,default='')

# Create your models here.
