# Generated by Django 2.2.16 on 2022-05-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0025_auto_20220504_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmpatientstatus',
            name='cause_of_death_other',
            field=models.TextField(blank=True, default='', verbose_name='Death details'),
        ),
        migrations.AlterField(
            model_name='mmpatientstatus',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Death'),
        ),
    ]
