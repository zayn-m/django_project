# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-29 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_comment_gamereview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='gamereview',
        ),
    ]