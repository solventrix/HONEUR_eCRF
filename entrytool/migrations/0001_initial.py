# Generated by Django 2.0.13 on 2020-09-29 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0038_auto_20191206_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdverseEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('lot', models.IntegerField(verbose_name='Line of Treatment')),
                ('severity', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V')], max_length=4, verbose_name='Severity')),
                ('ae_date', models.DateField(verbose_name='Date of AE')),
                ('adverse_event_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AEList',
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
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('hospital_number', models.CharField(blank=True, help_text='The unique identifier for this patient at the hospital.', max_length=255)),
                ('nhs_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='NHS Number')),
                ('surname', models.CharField(blank=True, max_length=255)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Date of Death')),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('gp_practice_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='GP Practice Code')),
                ('death_indicator', models.BooleanField(default=False, help_text='This field will be True if the patient is deceased.')),
                ('title_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('marital_status_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('birth_place_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('ethnicity_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('sex_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('birth_place_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Destination')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_demographics_subrecords', to=settings.AUTH_USER_MODEL)),
                ('ethnicity_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Ethnicity')),
                ('marital_status_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.MaritalStatus')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('sex_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Gender')),
                ('title_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opal.Title')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_demographics_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Demographics',
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('followup_date', models.DateField(default='1999-12-12', verbose_name='Visit date')),
                ('LDH', models.IntegerField(blank=True, null=True)),
                ('beta2m', models.IntegerField(blank=True, null=True)),
                ('albumin', models.IntegerField(blank=True, null=True)),
                ('creatinin', models.IntegerField(blank=True, null=True)),
                ('MCV', models.IntegerField(blank=True, null=True)),
                ('Hb', models.IntegerField(blank=True, null=True)),
                ('kappa_lambda_ratio', models.FloatField(blank=True, null=True)),
                ('bone_lesions', models.FloatField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_followup_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_followup_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('hospital', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Under Treatment', 'Under Treatment'), ('Dead', 'Dead'), ('Lost to Follow-up', 'Lost to Follow-up')], max_length=100, verbose_name='Patient Status')),
                ('diag_date', models.DateField(null=True, verbose_name='Date of Diagnosis')),
                ('smm_history', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='History of SMM')),
                ('smm_history_date', models.DateField(null=True, verbose_name='Date of SMM diagnosis')),
                ('mgus_history', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='History of MGUS')),
                ('mgus_history_date', models.DateField(null=True, verbose_name='Date of MGUS Diagnosis')),
                ('r_iss_stage', models.CharField(choices=[('Stage I', 'Stage I'), ('Stage II', 'Stage II'), ('Stage III', 'Stage III')], max_length=10, verbose_name='R-ISS Stage')),
                ('pp_type', models.CharField(choices=[('IgG', 'IgG'), ('IgA', 'IgA'), ('IgE', 'IgE'), ('Light Chain Myeloma', 'Light Chain Myeloma')], max_length=50, verbose_name='PP Type')),
                ('del_17p', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='del(17)p')),
                ('t4_14', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='t(4;14)')),
                ('t4_16', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='t(4;16)')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Date of Death')),
                ('death_cause', models.CharField(blank=True, choices=[('Disease', 'Disease'), ('Complications of Disease', 'Complications of Disease'), ('Other', 'Other')], max_length=100, null=True, verbose_name='Cause of Death')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_patientdetails_subrecords', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_patientdetails_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Regimen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('lot', models.IntegerField(verbose_name='Line of Treatment')),
                ('nbCycles', models.IntegerField(blank=True, null=True, verbose_name='Number of Cycles')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('stop_reason', models.CharField(blank=True, max_length=200, verbose_name='Reason for Regimen Stop')),
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
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('lot', models.IntegerField(verbose_name='Line of Treatment')),
                ('response_date', models.DateField()),
                ('response', models.CharField(choices=[('MR', 'Minimal response'), ('PR', 'Partial response'), ('VGPR', 'Very good partial response'), ('CR', 'Complete response'), ('SCR', 'Stringent complete response'), ('NCR', 'Near complete response'), ('ICR', 'Immunophenotypic complete response'), ('SD', 'Stable disease'), ('PD', 'Progressive disease'), ('RU', 'Response unknown')], max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_response_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_response_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SCT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('sct_date', models.DateField(verbose_name='Date of SCT')),
                ('sct_type', models.CharField(choices=[('Allogenic', 'Allogenic'), ('Autologous', 'Autologous'), ('Unknown', 'Unknown')], max_length=12, null=True, verbose_name='Type of SCT')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_sct_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_sct_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stem Cell Transplant',
                'verbose_name_plural': 'Stem Cell Transplants',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TreatmentLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('nb', models.IntegerField(verbose_name='Treatment Line')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_treatmentline_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_treatmentline_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
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
        migrations.AlterUniqueTogether(
            name='aelist',
            unique_together={('code', 'system')},
        ),
        migrations.AddField(
            model_name='adverseevent',
            name='adverse_event_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.AEList'),
        ),
        migrations.AddField(
            model_name='adverseevent',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_adverseevent_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adverseevent',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode'),
        ),
        migrations.AddField(
            model_name='adverseevent',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_adverseevent_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]
