# Generated by Django 3.2 on 2021-05-21 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0292_auto_20210520_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logdokqc',
            name='branch',
        ),
    ]
