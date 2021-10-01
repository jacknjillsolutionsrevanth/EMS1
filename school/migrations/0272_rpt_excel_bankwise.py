# Generated by Django 3.1.2 on 2021-04-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0271_center_actholdername'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpt_excel_bankwise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_number', models.CharField(blank=True, max_length=255, null=True)),
                ('supervisor', models.CharField(blank=True, max_length=255, null=True)),
                ('centre_code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('agent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bankno', models.CharField(blank=True, max_length=255, null=True)),
                ('bankname', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('ddate', models.DateField(blank=True, null=True)),
                ('net', models.FloatField(default=0.0)),
            ],
        ),
    ]