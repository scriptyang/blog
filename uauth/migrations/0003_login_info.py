# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uauth', '0002_delete_login_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=25)),
                ('addr', models.CharField(max_length=50)),
                ('login_time', models.DateTimeField(auto_now_add=True, verbose_name='login time')),
            ],
        ),
    ]