# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0021_auto_20180119_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lowshop',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='lowshop',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
