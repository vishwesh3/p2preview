# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-09 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2preview', '0008_auto_20171209_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityassigment',
            name='groupId',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='activityimageassigment',
            name='groupId',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
