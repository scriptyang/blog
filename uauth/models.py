from __future__ import unicode_literals

from django.db import models

class login_info(models.Model):
    user = models.CharField(max_length=25)
    addr = models.CharField(max_length=50)
    login_time = models.DateTimeField('login time', auto_now_add=True)

# Create your models here.
