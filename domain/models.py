# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Domain_info(models.Model):
    Type = models.CharField(max_length=20)
    Host = models.CharField(max_length=50)
    Value = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)

# Create your models here.
