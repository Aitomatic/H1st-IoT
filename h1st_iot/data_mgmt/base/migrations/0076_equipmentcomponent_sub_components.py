# Generated by Django 2.2.2 on 2019-06-26 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0075_remove_error_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentcomponent',
            name='sub_components',
            field=models.ManyToManyField(blank=True, related_name='equipment_components_reverse', related_query_name='equipment_component', to='H1stIoT_DataMgmt_Base.EquipmentComponent'),
        ),
    ]
