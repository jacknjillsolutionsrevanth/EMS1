# Generated by Django 3.2 on 2021-08-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0395_alter_rpt_emssumth_cid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpt_emssumth',
            name='cid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]