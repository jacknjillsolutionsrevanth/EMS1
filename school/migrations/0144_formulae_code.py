# Generated by Django 3.1.4 on 2020-12-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0143_auto_20201215_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulae',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]