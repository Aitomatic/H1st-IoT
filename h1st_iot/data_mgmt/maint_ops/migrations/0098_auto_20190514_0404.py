# Generated by Django 2.2.1 on 2019-05-14 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0097_auto_20190514_0353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='alarm_periods',
            new_name='equipment_instance_alarm_periods',
        ),
        migrations.RenameField(
            model_name='equipmentinstanceproblemdiagnosis',
            old_name='alarm_periods',
            new_name='equipment_instance_alarm_periods',
        ),
    ]