# Generated by Django 3.0.4 on 2021-08-08 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0400_rpt_emssumth_terace'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='girth',
        ),
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='height',
        ),
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='leaves',
        ),
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='terace',
        ),
        migrations.RemoveField(
            model_name='rpt_emssumth',
            name='teraceCnt',
        ),
    ]
