# Generated by Django 2.0.13 on 2020-10-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0012_auto_20201005_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdetails',
            name='lost_to_follow_up_date',
            field=models.DateField(blank=True, null=True, verbose_name='Lost to Follow-up '),
        ),
    ]
