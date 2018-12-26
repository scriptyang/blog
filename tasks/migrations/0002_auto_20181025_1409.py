# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='remote_cmd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmd', models.CharField(default='', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='command_list',
            new_name='local_cmd',
        ),
    ]