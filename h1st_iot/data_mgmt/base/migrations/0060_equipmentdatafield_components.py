# Generated by Django 2.2.1 on 2019-05-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0059_remove_equipmentdatafield_components'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentdatafield',
            name='components',
            field=models.ManyToManyField(blank=True, to='H1stIoT_DataMgmt_Base.EquipmentComponent'),
        ),
    ]
