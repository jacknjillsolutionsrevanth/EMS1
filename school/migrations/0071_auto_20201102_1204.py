# Generated by Django 3.1.2 on 2020-11-02 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0070_auto_20201102_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cloan',
            old_name='centername',
            new_name='center',
        ),
    ]
