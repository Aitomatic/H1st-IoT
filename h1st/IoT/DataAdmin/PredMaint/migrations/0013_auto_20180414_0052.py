# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0012_auto_20180410_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprint',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]