# Generated by Django 3.1.2 on 2020-11-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0078_daily_data_ltrs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='depositno',
        ),
        migrations.AddField(
            model_name='deposit',
            name='agent_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
