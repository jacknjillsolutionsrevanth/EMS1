# Generated by Django 3.2 on 2021-05-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0301_daily_data_remove'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('profit', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='center_name',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='comm',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='ltrrate',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='ltrs',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='ltrtsrate',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='net',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='pel',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='routecode',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='routename',
        ),
        migrations.RemoveField(
            model_name='dokqc_entry',
            name='tsrate',
        ),
    ]
