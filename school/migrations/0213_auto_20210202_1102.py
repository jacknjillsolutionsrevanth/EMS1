# Generated by Django 3.1.2 on 2021-02-02 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0212_auto_20210201_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='center',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='date',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='iamount',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='idate',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='installment_amt',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='interest_amt',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='ltrrate',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='net',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='noofinstallments',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='routecode',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='sdate',
        ),
        migrations.RemoveField(
            model_name='rpt_milkbillreport',
            name='total',
        ),
    ]
