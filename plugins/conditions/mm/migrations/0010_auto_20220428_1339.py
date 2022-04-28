# Generated by Django 2.0.13 on 2022-04-28 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0042_auto_20220421_1545'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mm', '0009_auto_20220428_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='MMPatientStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('status', models.CharField(blank=True, choices=[('Dead', 'Dead'), ('Lost', 'Lost'), ('Alive', 'Alive')], max_length=256, null=True, verbose_name='Status')),
                ('status_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('cause_of_death', models.CharField(blank=True, choices=[('Multiple Myeloma', 'Multiple Myeloma'), ('Infection', 'Infection'), ('Thrombosis', 'Thrombosis'), ('Not Disease Related', 'Not Disease Related'), ('Not Available', 'not available'), ('Other', 'Other')], max_length=256, null=True, verbose_name='Cause Of Death')),
                ('cause_of_death_other', models.TextField(blank=True, default='', verbose_name='Details')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_mmpatientstatus_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_mmpatientstatus_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Patient Status',
                'verbose_name_plural': 'Patient Statuses',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='patientoutcome',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='patientoutcome',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patientoutcome',
            name='updated_by',
        ),
        migrations.RenameField(
            model_name='mmdiagnosisdetails',
            old_name='cc_scale',
            new_name='icc_scale',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='epidemiologic_registry',
        ),
        migrations.AlterField(
            model_name='mmregimen',
            name='negative_mrd',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Negative EMR'),
        ),
        migrations.AlterField(
            model_name='mmregimen',
            name='negative_mrd_date',
            field=models.DateField(blank=True, null=True, verbose_name='Negative EMR Date'),
        ),
        migrations.DeleteModel(
            name='PatientOutcome',
        ),
    ]