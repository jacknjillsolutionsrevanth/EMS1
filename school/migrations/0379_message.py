# Generated by Django 3.2 on 2021-07-31 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0378_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('centre_code', models.CharField(max_length=255, null=True)),
                ('centercode', models.CharField(max_length=255, null=True)),
                ('can', models.FloatField(blank=True, default=0.0, null=True)),
                ('qty', models.FloatField(blank=True, default=0.0, null=True)),
                ('Email', models.CharField(blank=True, max_length=225, null=True)),
                ('fat', models.FloatField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]