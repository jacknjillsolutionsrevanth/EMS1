# Generated by Django 3.0.4 on 2021-07-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0350_auto_20210705_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='extractplantdata',
            name='extUser',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='extractplantdata',
            name='extdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
