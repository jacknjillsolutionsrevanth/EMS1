# Generated by Django 3.1.2 on 2021-02-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0220_dashboard_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='otp',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
