# Generated by Django 3.0.4 on 2021-08-28 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0415_auto_20210825_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_extractplantagdata',
            name='LivSum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rpt_extractplantagdata',
            name='TeraceCnt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rpt_extractplantagdata',
            name='blkCnt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]