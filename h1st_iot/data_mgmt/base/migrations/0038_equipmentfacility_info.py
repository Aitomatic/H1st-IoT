# Generated by Django 2.1.5 on 2019-02-12 02:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0037_auto_20190128_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentfacility',
            name='info',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]