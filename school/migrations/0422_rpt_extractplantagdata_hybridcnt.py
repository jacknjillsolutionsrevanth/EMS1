# Generated by Django 3.0.4 on 2021-09-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0421_rpt_extractplantagdata_cidh'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_extractplantagdata',
            name='hybridCnt',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
    ]