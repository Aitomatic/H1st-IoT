# Generated by Django 2.2.5 on 2019-10-03 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IoT_MaintOps', '0110_auto_20190726_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentuniquetypegroupmonitoreddatafieldconfig',
            name='equipment_unique_type_group_service_config',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_unique_type_group_monitored_data_field_configs', related_query_name='equipment_unique_type_group_monitored_data_field_config', to='IoT_MaintOps.EquipmentUniqueTypeGroupServiceConfig'),
        ),
    ]