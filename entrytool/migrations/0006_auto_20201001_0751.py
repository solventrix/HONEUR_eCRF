# Generated by Django 2.0.13 on 2020-10-01 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0005_auto_20200930_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adverseevent',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='lot',
        ),
        migrations.RemoveField(
            model_name='response',
            name='lot',
        ),
    ]
