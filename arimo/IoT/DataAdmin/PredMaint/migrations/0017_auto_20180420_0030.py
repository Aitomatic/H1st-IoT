# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0016_auto_20180420_0014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert',
            options={'ordering': ('equipment_general_type', 'equipment_unique_type_group', 'equipment_instance', 'risk_score_name', 'threshold')},
        ),
    ]
