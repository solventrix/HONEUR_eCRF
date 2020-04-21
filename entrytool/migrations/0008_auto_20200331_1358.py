# Generated by Django 2.0.13 on 2020-03-31 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0038_auto_20191206_1449'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entrytool', '0007_auto_20200331_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regimen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('lot', models.IntegerField(verbose_name='Line of Treatment')),
                ('nbCycles', models.IntegerField(blank=True, verbose_name='Number of Cycles')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, verbose_name='End Date')),
                ('stop_reason', models.CharField(max_length=200, verbose_name='Reason for Regimen Stop')),
                ('regimen_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_regimen_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RegimenList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='death_cause',
            field=models.CharField(choices=[('D', 'Disease'), ('C', 'Complications of Disease'), ('O', 'Other')], max_length=100, verbose_name='Cause of Death'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='death_date',
            field=models.DateField(null=True, verbose_name='Date of Death'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='del_17p',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('U', 'Unknown')], max_length=10, verbose_name='del(17)p'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='diag_date',
            field=models.DateField(null=True, verbose_name='Date of Diagnosis'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='mgus_history',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('U', 'Unknown')], max_length=10, verbose_name='History of MGUS'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='mgus_history_date',
            field=models.DateField(null=True, verbose_name='Date of MGUS Diagnosis'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='pp_type',
            field=models.CharField(choices=[('IgG', 'IgG'), ('IgA', 'IgA'), ('IgE', 'IgE'), ('LCM', 'Light Chain Myeloma')], max_length=50, verbose_name='PP Type'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='r_iss_stage',
            field=models.CharField(choices=[('1', 'Stage I'), ('2', 'Stage II'), ('3', 'Stage III')], max_length=10, verbose_name='R-ISS Stage'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='smm_history',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('U', 'Unknown')], max_length=10, verbose_name='History of SMM'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='smm_history_date',
            field=models.DateField(null=True, verbose_name='Date of SMM diagnosis'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='t4_14',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('U', 'Unknown')], max_length=10, verbose_name='t(4;14)'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='t4_16',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('U', 'Unknown')], max_length=10, verbose_name='t(4;16)'),
        ),
        migrations.AlterUniqueTogether(
            name='regimenlist',
            unique_together={('code', 'system')},
        ),
        migrations.AddField(
            model_name='regimen',
            name='regimen_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.RegimenList'),
        ),
        migrations.AddField(
            model_name='regimen',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_regimen_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]
