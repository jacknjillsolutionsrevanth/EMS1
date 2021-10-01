# Generated by Django 3.0.4 on 2020-09-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0030_auto_20200930_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=255, null=True)),
                ('good_sour', models.CharField(blank=True, max_length=255, null=True)),
                ('centre_code', models.CharField(blank=True, max_length=255, null=True)),
                ('milk_type', models.CharField(blank=True, max_length=255, null=True)),
                ('can', models.IntegerField(blank=True, null=True)),
                ('qty', models.FloatField(default=0.0)),
                ('exp', models.FloatField(default=0.0)),
                ('rate', models.FloatField(default=0.0)),
                ('fat', models.FloatField(default=0.0)),
                ('cartage', models.FloatField(default=0.0)),
                ('pen', models.FloatField(default=0.0)),
                ('clr', models.FloatField(default=0.0)),
                ('amount', models.FloatField(default=0.0)),
                ('total_amount', models.FloatField(default=0.0)),
                ('snf', models.FloatField(default=0.0)),
            ],
        ),
    ]
