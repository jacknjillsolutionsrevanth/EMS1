# Generated by Django 3.1.2 on 2021-01-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0196_auto_20210126_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='Route_attached',
            field=models.CharField(max_length=255),
        ),
    ]
