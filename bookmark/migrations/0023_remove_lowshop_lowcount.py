# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0022_auto_20180119_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lowshop',
            name='lowcount',
        ),
    ]
