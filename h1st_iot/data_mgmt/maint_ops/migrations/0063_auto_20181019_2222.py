# Generated by Django 2.1.1 on 2018-10-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0062_auto_20181018_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='equipment_problem_periods',
            new_name='equipment_diagnoses',
        ),
    ]
