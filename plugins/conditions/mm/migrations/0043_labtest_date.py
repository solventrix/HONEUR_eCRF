# Generated by Django 2.2.16 on 2023-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0042_auto_20230421_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtest',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]