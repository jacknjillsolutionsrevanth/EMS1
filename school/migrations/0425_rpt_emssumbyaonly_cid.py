# Generated by Django 3.2 on 2021-09-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0424_auto_20210922_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_emssumbyaonly',
            name='cid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
