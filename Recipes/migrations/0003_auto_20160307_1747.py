# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0002_auto_20160307_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicReturnText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_statement', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='generalaction',
            name='return_statement',
        ),
        migrations.AlterField(
            model_name='generalaction',
            name='instruction_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AddField(
            model_name='generalaction',
            name='basic_return_text',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Recipes.BasicReturnText'),
        ),
    ]
