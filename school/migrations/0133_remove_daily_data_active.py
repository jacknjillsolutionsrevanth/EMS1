# Generated by Django 3.1.3 on 2020-12-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0132_daily_data_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily_data',
            name='active',
        ),
    ]
