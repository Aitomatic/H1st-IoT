# Generated by Django 2.1.5 on 2019-02-01 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0080_auto_20190201_0350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            old_name='excluded_equipment_data_fields',
            new_name='manually_excluded_equipment_data_fields',
        ),
    ]
