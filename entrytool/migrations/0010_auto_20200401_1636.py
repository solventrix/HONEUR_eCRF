# Generated by Django 2.0.13 on 2020-04-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0009_auto_20200401_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regimen',
            name='nbCycles',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Cycles'),
        ),
    ]
