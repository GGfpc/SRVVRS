# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('texto', models.TextField(default='', max_length=10000)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]