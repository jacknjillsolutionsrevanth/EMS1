# Generated by Django 3.1.2 on 2021-03-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0250_rpt_daywiseabstract_routecode'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpt_daywiseabstract',
            name='pel',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]