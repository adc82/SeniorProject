# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsession',
            name='is_entering_conditional',
            field=models.BooleanField(default=False),
        ),
    ]
