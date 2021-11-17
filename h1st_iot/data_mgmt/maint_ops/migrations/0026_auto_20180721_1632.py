# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0025_auto_20180720_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='equipment_problem_periods',
            field=models.ManyToManyField(blank=True, to='H1stIoT_DataMgmt_MaintOps.EquipmentInstanceProblemDiagnosis'),
        ),
        migrations.AddField(
            model_name='equipmentinstanceproblemdiagnosis',
            name='alerts',
            field=models.ManyToManyField(blank=True, related_name='equipment_problem_instances', related_query_name='equipment_problem_instance', to='H1stIoT_DataMgmt_MaintOps.Alert'),
        ),
    ]