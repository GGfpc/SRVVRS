# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projs', '0003_auto_20160504_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecto',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='projecto',
            name='texto',
            field=models.TextField(default='', max_length=2000),
        ),
    ]