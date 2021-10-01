# Generated by Django 3.0.4 on 2021-08-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0408_extractplantdata_treeage'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpt_emsSumTHArOnly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaCode', models.CharField(blank=True, max_length=10, null=True)),
                ('blkCode', models.IntegerField(blank=True, default=0.0, null=True)),
                ('teraceNo', models.IntegerField(blank=True, default=0.0, null=True)),
                ('TotCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('DedCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('LivCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('eid', models.IntegerField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]