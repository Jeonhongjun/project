# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='search',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
