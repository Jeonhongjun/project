# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0020_lowshop_lowcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lowshop',
            name='created_time',
        ),
        migrations.AddField(
            model_name='lowshop',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
