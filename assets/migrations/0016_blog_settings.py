# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20181108_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
    ]