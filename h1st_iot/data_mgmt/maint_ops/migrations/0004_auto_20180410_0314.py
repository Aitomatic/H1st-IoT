# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-10 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_MaintOps', '0003_auto_20180410_0249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blueprint',
            options={'ordering': ('uuid', 'timestamp')},
        ),
        migrations.AddField(
            model_name='blueprint',
            name='uuid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
