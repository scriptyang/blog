# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-16 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20181016_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_info',
            name='end_time',
            field=models.CharField(max_length=255),
        ),
    ]
