# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0044_auto_20180904_1718'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MonitoredEquipmentDataFieldConfig',
            new_name='EquipmentUniqueTypeGroupMonitoredDataFieldConfig',
        ),
    ]
