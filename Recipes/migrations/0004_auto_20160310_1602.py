# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0003_auto_20160307_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appsession',
            name='current_app',
        ),
        migrations.RemoveField(
            model_name='appsession',
            name='user',
        ),
        migrations.DeleteModel(
            name='AppSession',
        ),
    ]