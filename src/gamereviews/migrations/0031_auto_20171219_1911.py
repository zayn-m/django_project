# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamereviews', '0030_auto_20171219_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='imgs',
            field=models.ImageField(default='static/images/None/no-img.jpg', upload_to='images/'),
        ),
    ]