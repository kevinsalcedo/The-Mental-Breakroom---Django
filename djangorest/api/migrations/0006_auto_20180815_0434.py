# Generated by Django 2.1 on 2018-08-15 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180815_0423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disorder',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='disorder',
            name='date_modified',
        ),
    ]