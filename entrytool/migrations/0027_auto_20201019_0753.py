# Generated by Django 2.0.13 on 2020-10-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0026_auto_20201016_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='followup',
            name='Hb',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='MCV',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='bone_lesions',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='creatinin',
        ),
        migrations.RemoveField(
            model_name='followup',
            name='kappa_lambda_ratio',
        ),
        migrations.AddField(
            model_name='followup',
            name='mprotein_serum',
            field=models.FloatField(blank=True, null=True, verbose_name='MProtein Serum'),
        ),
        migrations.AddField(
            model_name='followup',
            name='mprotein_urine',
            field=models.FloatField(blank=True, null=True, verbose_name='MProtein Urine'),
        ),
    ]
