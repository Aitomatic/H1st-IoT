# Generated by Django 2.1.5 on 2019-02-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0049_auto_20190223_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstancedailymetadata',
            name='date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
    ]
