# Generated by Django 2.1 on 2018-08-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20180820_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.CharField(max_length=5000, unique=True),
        ),
    ]
