# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echo', '0005_auto_20160307_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='line_spname',
            field=models.CharField(choices=[('\u4e2d\u56fd\u7535\u4fe1', '\u4e2d\u56fd\u7535\u4fe1'), ('\u4e2d\u56fd\u8054\u901a', '\u4e2d\u56fd\u8054\u901a'), ('\u4e2d\u56fd\u79fb\u52a8', '\u4e2d\u56fd\u79fb\u52a8'), ('\u4e2d\u56fd\u94c1\u901a', '\u4e2d\u56fd\u94c1\u901a'), ('\u5176\u4ed6', '\u5176\u4ed6')], default='\u4fe1\u7f51\u516c\u53f8', max_length=10, verbose_name='\u8fd0\u8425\u5546'),
        ),
    ]
