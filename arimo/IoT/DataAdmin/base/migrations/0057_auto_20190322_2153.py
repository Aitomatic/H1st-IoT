# Generated by Django 2.1.5 on 2019-03-22 21:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0056_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='value',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None),
            preserve_default=False,
        ),
    ]
