# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-24 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_auto_20160921_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
