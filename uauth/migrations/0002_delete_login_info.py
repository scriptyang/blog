# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 07:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uauth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login_info',
        ),
    ]