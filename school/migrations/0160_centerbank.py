# Generated by Django 3.1.4 on 2021-01-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0159_auto_20210105_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='centerbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('Shift', models.CharField(max_length=255)),
                ('centercode', models.CharField(max_length=255)),
                ('bankno', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=255, null=True)),
                ('Milktype', models.CharField(max_length=255)),
                ('kgs', models.FloatField(default=0.0)),
                ('Ltrs', models.FloatField(default=0.0)),
                ('Fat', models.FloatField(default=0.0)),
                ('Snf', models.FloatField(default=0.0)),
                ('RateLTR', models.FloatField(default=0.0)),
                ('Netamount', models.FloatField(default=0.0)),
                ('PiExp', models.FloatField(default=0.0)),
                ('Total', models.FloatField(default=0.0)),
            ],
        ),
    ]
