# Generated by Django 2.1.1 on 2018-10-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arimo_IoT_DataAdmin_PredMaint', '0060_auto_20180925_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertdiagnosisstatus',
            name='name',
            field=models.CharField(default='to_diagnose', max_length=255, unique=True),
        ),
    ]
