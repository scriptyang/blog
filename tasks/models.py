# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Task_info(models.Model):
    command = models.CharField(help_text='操作命令',max_length=500)
    start_time = models.CharField(max_length=255)
    user = models.CharField(max_length=50,default='user')
    content = models.TextField(default='')

class local_cmd(models.Model):
    cmd = models.CharField(max_length=255)

class remote_cmd(models.Model):
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)

class re_cm(models.Model):
    cmd = models.CharField(max_length=255)

# Create your models here.
