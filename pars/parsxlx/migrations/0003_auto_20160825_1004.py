# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsxlx', '0002_workbook_som'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workbook',
            name='som',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]