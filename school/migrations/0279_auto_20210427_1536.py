# Generated by Django 3.1.4 on 2021-04-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0278_auto_20210416_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='kgtsrate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='rpt_consolidatedreport',
            name='ltrtsrate',
            field=models.FloatField(default=0.0),
        ),
    ]