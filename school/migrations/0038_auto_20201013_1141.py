# Generated by Django 3.1.2 on 2020-10-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0037_auto_20201013_1058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily_data',
            old_name='date',
            new_name='datefrom',
        ),
        migrations.RenameField(
            model_name='daily_data',
            old_name='shift_loc',
            new_name='shift_from',
        ),
        migrations.AddField(
            model_name='daily_data',
            name='dateto',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='daily_data',
            name='shift_to',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
