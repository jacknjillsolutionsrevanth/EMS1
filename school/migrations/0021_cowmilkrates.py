# Generated by Django 3.0.4 on 2020-09-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0020_auto_20200929_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='CowMilkRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('rate_calculation', models.CharField(blank=True, max_length=255, null=True)),
                ('snf_value', models.CharField(blank=True, max_length=255, null=True)),
                ('fixed_value', models.IntegerField(blank=True, null=True)),
                ('min_fat', models.CharField(blank=True, max_length=255, null=True)),
                ('max_fat', models.CharField(blank=True, max_length=255, null=True)),
                ('min_SNF', models.CharField(blank=True, max_length=255, null=True)),
                ('max_SNF', models.CharField(blank=True, max_length=255, null=True)),
                ('rate', models.CharField(blank=True, max_length=255, null=True)),
                ('commission', models.CharField(blank=True, max_length=255, null=True)),
                ('snf_deduction', models.BooleanField(default=True)),
                ('fat_from', models.CharField(blank=True, max_length=255, null=True)),
                ('fat_to', models.CharField(blank=True, max_length=255, null=True)),
                ('penalty_in_RS', models.CharField(blank=True, max_length=255, null=True)),
                ('deduction_calculation', models.CharField(blank=True, max_length=255, null=True)),
                ('premium', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('commission_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sour_milk', models.CharField(blank=True, max_length=255, null=True)),
                ('curd', models.IntegerField(blank=True, null=True)),
                ('min_rate', models.IntegerField(blank=True, null=True)),
                ('sour_milkrate', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]