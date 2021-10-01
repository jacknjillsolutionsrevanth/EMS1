# Generated by Django 3.0.4 on 2021-09-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0418_auto_20210829_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='rpt_emsSumbyH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaCode', models.CharField(blank=True, max_length=10, null=True)),
                ('blkCode', models.CharField(blank=True, max_length=10, null=True)),
                ('teraceNo', models.CharField(blank=True, max_length=10, null=True)),
                ('plantType', models.CharField(blank=True, max_length=10, null=True)),
                ('TotCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('DedCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('LivCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('TeraceCnt', models.IntegerField(blank=True, default=0.0, null=True)),
                ('eid', models.IntegerField(blank=True, default=0.0, null=True)),
                ('cid', models.IntegerField(blank=True, default=0, null=True)),
                ('LivSum', models.IntegerField(blank=True, default=0.0, null=True)),
                ('hybridCnt', models.IntegerField(blank=True, default=0.0, null=True)),
            ],
        ),
    ]