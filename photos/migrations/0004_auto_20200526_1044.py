# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-26 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20200523_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='thumb',
            field=models.ImageField(default=None, upload_to='media/'),
        ),
    ]
