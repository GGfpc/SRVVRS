# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projs', '0006_auto_20160509_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='imagem',
            field=models.TextField(default='', max_length=300),
        ),
    ]
