# Generated by Django 3.0.4 on 2021-07-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0376_rpt_emsrevsum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpt_emsrevsum',
            name='YMth',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
