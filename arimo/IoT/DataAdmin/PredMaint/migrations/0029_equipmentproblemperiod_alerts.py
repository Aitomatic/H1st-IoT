# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0028_auto_20180721_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentproblemperiod',
            name='alerts',
            field=models.ManyToManyField(blank=True, to='Arimo_IoT_DataAdmin_PredMaint.Alert'),
        ),
    ]
