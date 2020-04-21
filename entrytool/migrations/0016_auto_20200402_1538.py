# Generated by Django 2.0.13 on 2020-04-02 13:38

from django.db import migrations, models
import django.db.models.deletion
import entrytool.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0038_auto_20191206_1449'),
        ('entrytool', '0015_auto_20200402_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('episode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=('opal.episode',),
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='lot_fk',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='lot_ft',
        ),
        migrations.AddField(
            model_name='followup',
            name='Hb',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='LDH',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='MCV',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='albumin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='beta2m',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='bone_lesions',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='creatinin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='kappa_lambda_ratio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regimen',
            name='lot',
            field=models.IntegerField(default=0, validators=[entrytool.models.validate_positive], verbose_name='Line of Treatment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='lot',
            field=models.IntegerField(default=0, verbose_name='Line of Treatment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='regimen',
            name='nbCycles',
            field=models.IntegerField(blank=True, null=True, validators=[entrytool.models.validate_positive], verbose_name='Number of Cycles'),
        ),
    ]
