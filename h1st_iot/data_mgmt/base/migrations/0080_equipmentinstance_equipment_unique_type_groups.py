# Generated by Django 2.2.2 on 2019-06-27 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0079_auto_20190626_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinstance',
            name='equipment_unique_type_groups',
            field=models.ManyToManyField(blank=True, related_name='equipment_instances', related_query_name='equipment_instance', to='H1stIoT_DataMgmt_Base.EquipmentUniqueTypeGroup'),
        ),
    ]
