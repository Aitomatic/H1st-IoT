# Generated by Django 2.1.5 on 2019-02-24 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0055_auto_20190224_0155'),
        ('H1stIoT_DataMgmt_MaintOps', '0092_auto_20190224_0442'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='equipmentproblemperiod',
            unique_together={('equipment_instance', 'to_date'), ('equipment_instance', 'from_date')},
        ),
    ]
