# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
