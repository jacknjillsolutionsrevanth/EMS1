# Generated by Django 3.0.4 on 2021-09-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0420_rpt_extractplantthagdata_cidh'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_extractplantagdata',
            name='cidH',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]