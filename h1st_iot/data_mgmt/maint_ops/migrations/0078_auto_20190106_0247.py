# Generated by Django 2.1.4 on 2019-01-06 02:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0077_equipmentuniquetypegroupserviceconfig_configs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentuniquetypegroupserviceconfig',
            name='configs',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
    ]