# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0003_auto_20181214_1254'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comments',
            unique_together=set([]),
        ),
    ]