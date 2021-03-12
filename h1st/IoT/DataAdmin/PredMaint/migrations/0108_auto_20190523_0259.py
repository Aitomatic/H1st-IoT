# Generated by Django 2.2.1 on 2019-05-23 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0074_auto_20190522_1956'),
        ('Arimo_IoT_DataAdmin_PredMaint', '0107_remove_alertdiagnosisstatus_last_updated'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='equipmentinstancealarmperiod',
            unique_together={('equipment_instance', 'alarm_type', 'from_utc_date_time')},
        ),
        migrations.AlterUniqueTogether(
            name='equipmentproblemperiod',
            unique_together={('equipment_instance', 'from_date')},
        ),
    ]