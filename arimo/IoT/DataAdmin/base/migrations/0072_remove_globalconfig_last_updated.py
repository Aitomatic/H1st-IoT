# Generated by Django 2.2.1 on 2019-05-20 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_Base', '0071_auto_20190516_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalconfig',
            name='last_updated',
        ),
    ]