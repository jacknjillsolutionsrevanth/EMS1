# Generated by Django 3.2 on 2021-06-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0334_rpt_loan_installment_amt'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_loan',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
