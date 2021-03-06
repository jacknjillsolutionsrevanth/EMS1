# Generated by Django 3.1.2 on 2020-10-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0043_auto_20201013_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyproc',
            name='datefrom',
        ),
        migrations.RemoveField(
            model_name='dailyproc',
            name='dateto',
        ),
        migrations.RemoveField(
            model_name='dailyproc',
            name='shift_from',
        ),
        migrations.RemoveField(
            model_name='dailyproc',
            name='shift_to',
        ),
        migrations.AddField(
            model_name='daily_data',
            name='datefrom',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='dateto',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='shift_from',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='shift_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
