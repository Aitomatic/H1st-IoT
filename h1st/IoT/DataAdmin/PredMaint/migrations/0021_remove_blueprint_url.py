# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0020_auto_20180420_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blueprint',
            name='url',
        ),
    ]