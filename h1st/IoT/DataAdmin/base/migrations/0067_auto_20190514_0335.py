# Generated by Django 2.2.1 on 2019-05-14 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0066_auto_20190514_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipmentuniquetype',
            old_name='data_fields',
            new_name='equipment_data_fields',
        ),
    ]