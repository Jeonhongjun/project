# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0018_lowshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='lowshop',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
