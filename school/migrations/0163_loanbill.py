# Generated by Django 3.1.2 on 2021-01-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0162_auto_20210116_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loanbill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateField(blank=True, null=True)),
                ('idate', models.DateField(blank=True, null=True)),
                ('routecode', models.CharField(blank=True, max_length=255, null=True)),
                ('centercode', models.CharField(blank=True, max_length=255, null=True)),
                ('installment_amt', models.FloatField(default=0.0)),
                ('interest_amt', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('noofinstallments', models.FloatField(default=0.0)),
            ],
        ),
    ]