# Generated by Django 2.0.13 on 2020-10-07 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0015_auto_20201007_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demographics',
            options={'verbose_name': 'Demographics', 'verbose_name_plural': 'Demographics'},
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_adverseevent_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode'),
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='adverseevent',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_adverseevent_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_demographics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='death_indicator',
            field=models.BooleanField(default=False, help_text='This field will be True if the patient is deceased.', verbose_name='Death Indicator'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='hospital_number',
            field=models.CharField(blank=True, help_text='The unique identifier for this patient at the hospital.', max_length=255, verbose_name='Demographics'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='post_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Post Code'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='surname',
            field=models.CharField(blank=True, max_length=255, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_demographics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='Hb',
            field=models.FloatField(blank=True, null=True, verbose_name='Hb'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='LDH',
            field=models.FloatField(blank=True, null=True, verbose_name='LDH'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='MCV',
            field=models.FloatField(blank=True, null=True, verbose_name='MCV'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='albumin',
            field=models.FloatField(blank=True, null=True, verbose_name='Albumin'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='beta2m',
            field=models.FloatField(blank=True, null=True, verbose_name='beta2m'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='bone_lesions',
            field=models.FloatField(blank=True, null=True, verbose_name='Bone Lesions'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_followup_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='creatinin',
            field=models.FloatField(blank=True, null=True, verbose_name='Creatinin'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='kappa_lambda_ratio',
            field=models.FloatField(blank=True, null=True, verbose_name='Kappa Lambda Ratio'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_followup_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_patientdetails_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='patientdetails',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_patientdetails_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='regimen',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='regimen',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='regimen',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_regimen_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='regimen',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode'),
        ),
        migrations.AlterField(
            model_name='regimen',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='regimen',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_regimen_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='response',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='response',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='response',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_response_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='response',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.CharField(choices=[(('Minimal response', 'Minimal response'), ('Minimal response', 'Minimal response')), (('Partial response', 'Partial response'), ('Partial response', 'Partial response')), (('Very good partial response', 'Very good partial response'), ('Very good partial response', 'Very good partial response')), (('Complete response', 'Complete response'), ('Complete response', 'Complete response')), (('Stringent complete response', 'Stringent complete response'), ('Stringent complete response', 'Stringent complete response')), (('Near complete response', 'Near complete response'), ('Near complete response', 'Near complete response')), (('Immunophenotypic complete response', 'Immunophenotypic complete response'), ('Immunophenotypic complete response', 'Immunophenotypic complete response')), (('Stable disease', 'Stable disease'), ('Stable disease', 'Stable disease')), (('Progressive disease', 'Progressive disease'), ('Progressive disease', 'Progressive disease')), (('Response unknown', 'Response unknown)'), ('Response unknown', 'Response unknown)'))], max_length=50, verbose_name='Response'),
        ),
        migrations.AlterField(
            model_name='response',
            name='response_date',
            field=models.DateField(verbose_name='Response Date'),
        ),
        migrations.AlterField(
            model_name='response',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='response',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_response_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='sct',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='sct',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='sct',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_sct_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='sct',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode'),
        ),
        migrations.AlterField(
            model_name='sct',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='sct',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_sct_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
        migrations.AlterField(
            model_name='treatmentline',
            name='consistency_token',
            field=models.CharField(max_length=8, verbose_name='Consistency Token'),
        ),
        migrations.AlterField(
            model_name='treatmentline',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='treatmentline',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_treatmentline_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='treatmentline',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode'),
        ),
        migrations.AlterField(
            model_name='treatmentline',
            name='updated',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='treatmentline',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_treatmentline_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
    ]
