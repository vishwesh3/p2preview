# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-08 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2preview', '0003_registeredgroupsforactivity_activityid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=45),
        ),
    ]