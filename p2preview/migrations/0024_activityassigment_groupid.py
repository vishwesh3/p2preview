# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2preview', '0023_auto_20171101_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityassigment',
            name='groupId',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
