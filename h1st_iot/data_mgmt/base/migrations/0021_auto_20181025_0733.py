# Generated by Django 2.1.1 on 2018-10-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H1stIoT_DataMgmt_Base', '0020_remove_equipmentdatafield_nullable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Data Type Name'),
        ),
        migrations.AlterField(
            model_name='equipmentdatafield',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Equipment Data Field Name'),
        ),
        migrations.AlterField(
            model_name='equipmentdatafieldtype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Equipment Data Field Type Name'),
        ),
        migrations.AlterField(
            model_name='equipmentfacility',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Equipment Facility Name'),
        ),
        migrations.AlterField(
            model_name='equipmentgeneraltype',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Equipment General Type Name'),
        ),
        migrations.AlterField(
            model_name='equipmentinstance',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Equipment Instance Name'),
        ),
        migrations.AlterField(
            model_name='equipmentsystem',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Equipment System Name'),
        ),
        migrations.AlterField(
            model_name='equipmentuniquetype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Equipment Unique Type Name'),
        ),
        migrations.AlterField(
            model_name='equipmentuniquetypegroup',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Equipment Unique Type Group Name'),
        ),
        migrations.AlterField(
            model_name='numericmeasurementunit',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Numeric Measurement Unit Name'),
        ),
    ]
