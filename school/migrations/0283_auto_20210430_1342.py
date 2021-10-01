# Generated by Django 3.2 on 2021-04-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0282_rpt_dailydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpt_dailydata',
            name='sampno',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rpt_dailydata',
            name='sampno2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rpt_excel_bankwise',
            name='net',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
