# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0006_auto_20180118_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('bookmark_id', models.AutoField(primary_key=True, serialize=False)),
                ('bookmark_name', models.CharField(max_length=100)),
                ('bookmark_url', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]
