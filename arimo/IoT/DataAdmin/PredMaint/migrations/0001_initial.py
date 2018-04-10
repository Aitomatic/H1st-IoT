# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-10 07:51
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, unique=True)),
                ('benchmark_metrics', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'ordering': ('url',),
            },
        ),
    ]
