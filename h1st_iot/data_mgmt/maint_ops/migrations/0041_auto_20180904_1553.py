# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0040_auto_20180904_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentuniquetypegroupserviceconfig',
            options={'ordering': ('-active', 'equipment_general_type', 'equipment_unique_type_group')},
        ),
    ]
