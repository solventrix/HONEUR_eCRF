# Generated by Django 2.0.13 on 2022-02-24 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entrytool', '0045_auto_20220224_1304'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0040_auto_20201007_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='MMDiagnosisDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('diag_date', models.DateField(null=True, verbose_name='Date of Diagnosis')),
                ('smm_history', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='History of SMM')),
                ('smm_history_date', models.DateField(blank=True, null=True, verbose_name='Date of SMM diagnosis')),
                ('mgus_history', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='History of MGUS')),
                ('mgus_history_date', models.DateField(blank=True, null=True, verbose_name='Date of MGUS Diagnosis')),
                ('iss_stage', models.CharField(choices=[('Stage I', 'Stage I'), ('Stage II', 'Stage II'), ('Stage III', 'Stage III'), ('Unknown', 'Unknown')], max_length=10, verbose_name='ISS Stage')),
                ('ds_stage', models.CharField(choices=[('Stage I', 'Stage I'), ('Stage II', 'Stage II'), ('Stage III', 'Stage III'), ('Unknown', 'Unknown')], max_length=10, verbose_name='DS Stage')),
                ('pp_type', models.CharField(choices=[('IgG', 'IgG'), ('IgA', 'IgA'), ('IgE', 'IgE'), ('Light Chain Myeloma', 'Light Chain Myeloma')], max_length=50, verbose_name='PP Type')),
                ('del_17p', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='del(17)p')),
                ('del_13', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='del13')),
                ('t4_14', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='t(4;14)')),
                ('t4_16', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='t(4;16)')),
                ('hospital_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_mmdiagnosisdetails_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('hospital_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.Hospital')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_mmdiagnosisdetails_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Diagnosis Details',
                'verbose_name_plural': 'Diagnosis Details',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MMFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('follow_up_date', models.DateField(verbose_name='Visit date')),
                ('LDH', models.FloatField(blank=True, null=True, verbose_name='LDH')),
                ('beta2m', models.FloatField(blank=True, null=True, verbose_name='beta2m')),
                ('albumin', models.FloatField(blank=True, null=True, verbose_name='Albumin')),
                ('mprotein_urine', models.FloatField(blank=True, null=True, verbose_name='MProtein Urine')),
                ('mprotein_serum', models.FloatField(blank=True, null=True, verbose_name='MProtein Serum')),
                ('mprotein_24h', models.FloatField(blank=True, null=True, verbose_name='Mprotein in 24 hour urine')),
                ('hospital_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_mmfollowup_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('hospital_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.Hospital')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_mmfollowup_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Follow-up',
                'verbose_name_plural': 'Follow-ups',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MMRegimen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('nbCycles', models.IntegerField(blank=True, null=True, verbose_name='Number of Cycles')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('category', models.CharField(choices=[('Induction', 'Induction'), ('Maintenance', 'Maintenance'), ('Conditioning', 'Conditioning'), ('Watch and wait', 'Watch and wait')], max_length=40, verbose_name='Regimen Type')),
                ('hospital_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('regimen_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('stop_reason_ft', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_mmregimen_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('hospital_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.Hospital')),
            ],
            options={
                'verbose_name': 'Regimen',
                'verbose_name_plural': 'Regimens',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MMRegimenList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('system', models.CharField(blank=True, max_length=255, null=True, verbose_name='System')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Code')),
                ('version', models.CharField(blank=True, max_length=255, null=True, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'MM Regimen List',
                'verbose_name_plural': 'MM Regimen List',
            },
        ),
        migrations.CreateModel(
            name='MMResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('response_date', models.DateField(verbose_name='Response Date')),
                ('response', models.CharField(choices=[('Minimal response', 'Minimal response'), ('Partial response', 'Partial response'), ('Very good partial response', 'Very good partial response'), ('Complete response', 'Complete response'), ('Stringent complete response', 'Stringent complete response'), ('Near complete response', 'Near complete response'), ('Immunophenotypic complete response', 'Immunophenotypic complete response'), ('Stable disease', 'Stable disease'), ('Progressive disease', 'Progressive disease'), ('Response unknown/NA', 'Response unknown/NA')], max_length=50, verbose_name='Response')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_mmresponse_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_mmresponse_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Response',
                'verbose_name_plural': 'Responses',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MMStopReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('system', models.CharField(blank=True, max_length=255, null=True, verbose_name='System')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Code')),
                ('version', models.CharField(blank=True, max_length=255, null=True, verbose_name='Version')),
            ],
            options={
                'verbose_name': 'MM Stop Reason List',
                'verbose_name_plural': 'MM Stop Reason List',
            },
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='regimen_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mm.MMRegimenList'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='stop_reason_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mm.MMStopReason'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_mmregimen_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By'),
        ),
    ]