# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recipes', '0006_auto_20160322_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionalBranch',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Recipes.Recipe')),
                ('branch_number', models.IntegerField()),
            ],
            bases=('Recipes.recipe',),
        ),
        migrations.CreateModel(
            name='ConditionalHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='generalaction',
            name='type',
            field=models.CharField(choices=[('NS', 'Not Specified'), ('RT', 'Basic Return Text'), ('C', 'Conditional')], default='RT', max_length=2),
        ),
        migrations.AddField(
            model_name='conditionalbranch',
            name='parent_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='Recipes.ConditionalHeader'),
        ),
        migrations.AddField(
            model_name='generalaction',
            name='conditional',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_action', to='Recipes.ConditionalHeader'),
        ),
    ]
