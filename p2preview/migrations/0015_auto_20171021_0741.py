# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 07:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('p2preview', '0014_auto_20171020_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredgroupsforactivity',
            name='lastLogined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]