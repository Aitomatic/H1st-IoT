# Generated by Django 2.1.5 on 2019-02-22 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0045_equipmentinstancedailymetadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentinstancedailymetadata',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]