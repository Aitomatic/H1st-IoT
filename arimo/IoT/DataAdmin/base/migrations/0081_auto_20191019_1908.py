# Generated by Django 2.2.6 on 2019-10-19 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0080_equipmentinstance_equipment_unique_type_groups'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='equipmentinstancedailymetadata',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='equipmentinstancedailymetadata',
            name='equipment_instance',
        ),
        migrations.DeleteModel(
            name='Error',
        ),
        migrations.DeleteModel(
            name='EquipmentInstanceDailyMetadata',
        ),
    ]
