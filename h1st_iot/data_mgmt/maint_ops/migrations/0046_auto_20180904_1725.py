# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0045_auto_20180904_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='equipment_unique_type_group_service_config',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='equipment_unique_type_group_monitored_data_field_configs', related_query_name='equipment_unique_type_group_monitored_data_field_config', to='H1stIoT_DataMgmt_MaintOps.EquipmentUniqueTypeGroupServiceConfig'),
        ),
        migrations.AlterField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='excluded_equipment_data_fields',
            field=models.ManyToManyField(blank=True, related_name='equipment_unique_type_group_monitored_data_field_configs_excl', related_query_name='equipment_unique_type_group_monitored_data_field_config_excl', to='H1stIoT_DataMgmt_Base.EquipmentDataField'),
        ),
        migrations.AlterField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='monitored_equipment_data_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_unique_type_group_monitored_data_field_configs', related_query_name='equipment_unique_type_group_monitored_data_field_config', to='H1stIoT_DataMgmt_Base.EquipmentDataField'),
        ),
    ]