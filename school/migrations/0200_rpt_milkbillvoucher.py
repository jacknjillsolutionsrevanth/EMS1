# Generated by Django 3.1.2 on 2021-01-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0199_auto_20210126_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='RPT_Milkbillvoucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routecode', models.IntegerField(blank=True, null=True)),
                ('routename', models.CharField(blank=True, max_length=255, null=True)),
                ('centre_code', models.IntegerField(blank=True, null=True)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('centername', models.CharField(blank=True, max_length=255, null=True)),
                ('centercode', models.IntegerField(blank=True, null=True)),
                ('Shift', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('milk_type', models.CharField(blank=True, max_length=255, null=True)),
                ('kgs', models.FloatField(default=0.0)),
                ('ltrs', models.FloatField(default=0.0)),
                ('amount', models.FloatField(default=0.0)),
                ('ltrrate', models.FloatField(default=0.0)),
                ('fat', models.FloatField(default=0.0)),
                ('snf', models.FloatField(default=0.0)),
                ('qty', models.FloatField(default=0.0)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('bankno', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_branch', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=255, null=True)),
                ('bankname', models.CharField(blank=True, max_length=255, null=True)),
                ('pel', models.FloatField(default=0.0)),
                ('net', models.FloatField(default=0.0)),
                ('agent_name', models.CharField(max_length=255)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('pin', models.IntegerField(blank=True, null=True)),
                ('sdate', models.DateField(blank=True, null=True)),
                ('idate', models.DateField(blank=True, null=True)),
                ('installment_amt', models.FloatField(default=0.0)),
                ('interest_amt', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('payable', models.FloatField(default=0.0)),
            ],
        ),
    ]