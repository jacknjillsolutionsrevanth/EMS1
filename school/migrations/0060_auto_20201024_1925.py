# Generated by Django 3.1.2 on 2020-10-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0059_auto_20201024_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dok_entry',
            name='bank_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dok_entry',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]