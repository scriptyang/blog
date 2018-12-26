# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-16 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_service_info_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(help_text='\u64cd\u4f5c\u547d\u4ee4', max_length=500)),
                ('start_time', models.DateField()),
                ('action_time', models.FloatField(help_text='\u6267\u884c\u65f6\u95f4')),
                ('end_time', models.DateField()),
            ],
        ),
    ]