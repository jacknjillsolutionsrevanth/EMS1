# Generated by Django 3.0.4 on 2020-09-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_auto_20200929_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='centerimage'),
        ),
    ]
