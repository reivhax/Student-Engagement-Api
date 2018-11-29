# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-29 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagementApp', '0002_remove_articles_highlighted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='Content',
            new_name='content',
        ),
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='articles',
            name='liked',
            field=models.BooleanField(default=True),
        ),
    ]
