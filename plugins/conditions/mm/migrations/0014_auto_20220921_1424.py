# Generated by Django 2.2.16 on 2022-09-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0013_auto_20220915_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='r_iss_stage',
            field=models.CharField(blank=True, choices=[('I', 'I'), ('II', 'II'), ('III', 'III')], max_length=10, null=True, verbose_name='r-ISS at ED'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='radiotherapy',
            field=models.BooleanField(default=False, verbose_name='Radiotherapy'),
        ),
    ]
