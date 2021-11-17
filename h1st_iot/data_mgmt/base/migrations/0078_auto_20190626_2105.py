# Generated by Django 2.2.2 on 2019-06-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0077_auto_20190626_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentcomponent',
            name='directly_interacts_with_components',
            field=models.ManyToManyField(blank=True, related_name='equipment_components_directly_interacts_reverse', related_query_name='equipment_component_directly_interacts_reverse', to='H1stIoT_DataMgmt_Base.EquipmentComponent'),
        ),
        migrations.AlterField(
            model_name='equipmentcomponent',
            name='sub_components',
            field=models.ManyToManyField(blank=True, related_name='equipment_components_sub_reverse', related_query_name='equipment_component_sub_reverse', to='H1stIoT_DataMgmt_Base.EquipmentComponent'),
        ),
    ]
