# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0023_remove_lowshop_lowcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowshop',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]
