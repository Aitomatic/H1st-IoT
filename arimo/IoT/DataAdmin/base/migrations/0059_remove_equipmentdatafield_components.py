# Generated by Django 2.2.1 on 2019-05-09 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0058_auto_20190509_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentdatafield',
            name='components',
        ),
    ]