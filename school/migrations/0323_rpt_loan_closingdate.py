# Generated by Django 3.2 on 2021-06-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0322_rpt_loan_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_loan',
            name='closingdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
