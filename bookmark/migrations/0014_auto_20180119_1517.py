# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0013_auto_20180119_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
