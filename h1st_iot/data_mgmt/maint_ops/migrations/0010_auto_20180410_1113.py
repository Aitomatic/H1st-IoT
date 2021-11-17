# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-10 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0009_auto_20180410_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprint',
            name='equipment_unique_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blueprints', related_query_name='blueprint', to='H1stIoT_DataMgmt_Base.EquipmentUniqueType'),
        ),
        migrations.AlterField(
            model_name='blueprint',
            name='timestamp',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='blueprint',
            name='trained_to_date',
            field=models.DateField(default=None),
        ),
    ]