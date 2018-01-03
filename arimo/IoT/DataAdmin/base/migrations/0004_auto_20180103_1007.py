# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-03 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0003_equipmentinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinstance',
            name='control_data_db_tbl',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='control_data_db_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='control_data_file_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='data_db_tbl',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='data_db_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='data_file_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='measure_data_db_tbl',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='measure_data_db_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='equipmentinstance',
            name='measure_data_file_url',
            field=models.URLField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
