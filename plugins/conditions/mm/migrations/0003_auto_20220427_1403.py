# Generated by Django 2.0.13 on 2022-04-27 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mm', '0002_mmpastmedicalhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoneDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('treatment_type', models.CharField(blank=True, choices=[('Denosumab', 'Denosumab'), ('Bisphosphonates Induction', 'Bisphosphonates Induction'), ('Vertebroplasty Induction', 'Vertebroplasty Induction'), ('Others Induction', 'Others Induction'), ('Not Available', 'Not Available')], max_length=256, null=True, verbose_name='Treatment Type')),
                ('bisphosphonate_treatment', models.CharField(blank=True, max_length=256, null=True, verbose_name='Bisphosphonate Treatment')),
                ('nb_cycles', models.IntegerField(blank=True, null=True, verbose_name='Number of Cycles')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('vertebroplasty_kyphoplasty_date', models.DateField(blank=True, null=True, verbose_name='Vertebroplasty Kyphoplasty Date')),
                ('vertebroplasty_kyphoplasty_description', models.TextField(blank=True, default='', verbose_name='Vertebroplasty Kyphoplasty Description')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_bonedisease_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_bonedisease_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Bone Disease Treatment',
                'verbose_name_plural': 'Bone Disease Treatments',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ConditionAtInduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('condition', models.CharField(blank=True, choices=[('Renal Failure', 'Renal Failure'), ('Neuropathy', 'Neuropathy'), ('Hemorrhage', 'Hemorrhage'), ('Fever', 'Fever'), ('Infection', 'Infection'), ('Other', 'Other')], max_length=256, null=True, verbose_name='Condition')),
                ('infection_type', models.CharField(blank=True, choices=[('Undocumented Preinfection', 'Undocumented Preinfection'), ('Microbiologically Documented Without Bacteremia', 'Microbiologically Documented Without Bacteremia'), ('Microbiologically Documented With Bacteremia', 'Microbiologically Documented With Bacteremia'), ('Clinically Documented', 'Clinically Documente')], max_length=256, null=True, verbose_name='Infection Type')),
                ('type_of_microorganism_infection', models.CharField(blank=True, max_length=256, null=True, verbose_name='Type Of Microorganism Infection')),
                ('infection_source', models.CharField(blank=True, max_length=256, null=True, verbose_name='Infection Source')),
                ('other_condition_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Condition Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_conditionatinduction_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_conditionatinduction_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Condition at induction',
                'verbose_name_plural': 'Conditions at induction',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Cytogenetics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('t4_14_not_effected', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='t(4;14) Not Effected')),
                ('t4_14_haploid_karyotype', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='t(4;14) Haploid Karyotype')),
                ('t4_14', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='t(4;14)')),
                ('t4_14_16', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='t(14;16)')),
                ('t11_14', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='t(11;14)')),
                ('del1p', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='del 1p')),
                ('del_17p', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, verbose_name='del(17)p')),
                ('gan1q', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='gan 1q')),
                ('chromosome_alterations', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='Chromosome Alterations')),
                ('normal_study', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='')),
                ('description', models.TextField(blank=True, default='', verbose_name='Description')),
                ('other_study', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='Other study')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_cytogenetics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_cytogenetics_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Cytogenetics',
                'verbose_name_plural': 'Cytogenetics',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Imaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('bone_series_test_image', models.CharField(blank=True, choices=[('Zero', 'Zero'), ('One', 'One'), ('Two', 'Two'), ('Three', 'Three')], max_length=256, null=True, verbose_name='Bone Series Test Image')),
                ('bone_series_description', models.TextField(blank=True, default='', verbose_name='Bone Series Description')),
                ('ct_scan', models.CharField(blank=True, choices=[('Negative', 'Negative'), ('Positive', 'Positive'), ('Not Done', 'Not Done')], max_length=256, null=True, verbose_name='CT Scan')),
                ('ct_scan_description', models.TextField(blank=True, default='', verbose_name='CT Scan Description')),
                ('resonance', models.CharField(blank=True, choices=[('Negative', 'Negative'), ('Positive', 'Positive'), ('Not Done', 'Not Done')], max_length=256, null=True, verbose_name='Resonance')),
                ('resonance_description', models.TextField(blank=True, default='', verbose_name='Resonance description')),
                ('pet_scan', models.CharField(blank=True, choices=[('Negative', 'Negative'), ('Positive', 'Positive'), ('Not Done', 'Not Done')], max_length=256, null=True, verbose_name='PET scan')),
                ('pet_scan_description', models.TextField(blank=True, default='', verbose_name='PET scan description')),
                ('other_imaging_test', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Other Imaging Test')),
                ('other_imaging_test_description', models.TextField(blank=True, default='', verbose_name='Other Imaging Test Description')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_imaging_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_imaging_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Imaging',
                'verbose_name_plural': 'Imaging',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LabTests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('pcr', models.IntegerField(blank=True, null=True, verbose_name='PCR')),
                ('celulas_plasmaticas_circulantes', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Celulas Plasmaticas Circulantes')),
                ('troponina', models.IntegerField(blank=True, null=True, verbose_name='Troponina')),
                ('total_proteins', models.IntegerField(blank=True, null=True, verbose_name='Total Proteins')),
                ('platelets', models.IntegerField(blank=True, null=True, verbose_name='Platelets')),
                ('beta_2_microglobulin', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Beta 2 Microglobulin')),
                ('alkaline_phosphatase', models.IntegerField(blank=True, null=True, verbose_name='Alkaline Phosphatase')),
                ('albumin', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Albumin')),
                ('creatinine', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Creatinine')),
                ('calcium', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Calcium')),
                ('hemoglobin', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Hemoglobin')),
                ('proteinuria', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Proteinuria')),
                ('proteinuria_g24', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Proteinuria gr/24')),
                ('leucocytes', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Leucocytes')),
                ('nt_pro_bnp', models.IntegerField(blank=True, null=True, verbose_name='NT-proBNP')),
                ('ldh', models.IntegerField(blank=True, null=True, verbose_name='LDH')),
                ('ldh_type', models.CharField(blank=True, max_length=256, null=True, verbose_name='LDH Type')),
                ('glomerular_filtration_formula_date', models.DateField(blank=True, null=True, verbose_name='Glomerular Filtration Formula Date')),
                ('glomerular_filtration_formula', models.CharField(blank=True, choices=[('MDRD', 'MDRD'), ('CKD-EPI', 'CKD-EPI'), ('Other', 'Other')], max_length=256, null=True, verbose_name='Glomerular Filtration Formula')),
                ('glomerular_filtration', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Glomerular Filtration')),
                ('filter_formula_description', models.TextField(blank=True, default='', verbose_name='Filter Formula Description')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_labtests_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_labtests_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MProteinMesurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('serum_amount', models.CharField(blank=True, max_length=256, null=True, verbose_name='Monoclonal serum amount')),
                ('heavy_chain_type', models.CharField(blank=True, choices=[('IgG', 'IgG'), ('IgD', 'IgD'), ('IgA', 'IgA'), ('IgM', 'IgM'), ('IgE', 'IgE'), ('No Heavy Chain', 'No Heavy Chain'), ('Other', 'Other')], max_length=256, null=True, verbose_name='Heavy Chain Type')),
                ('heavy_chain_type_other', models.CharField(blank=True, max_length=256, null=True, verbose_name='Heavy Chain Type Other')),
                ('light_chain_type', models.CharField(blank=True, choices=[('IgA', 'IgA'), ('IgD', 'IgD'), ('IgE', 'IgE'), ('IgG', 'IgG'), ('IgM', 'IgM')], max_length=256, null=True, verbose_name='Light Chain Type')),
                ('lambda_light_chain_count', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Lambda Light Chain Count')),
                ('kappa_light_chain_count', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Kappa Light Chain Count')),
                ('kappa_lambda_ratio', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Kappa Lambda Ratio')),
                ('urinary_monoclonal_count', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Urinary Monoclonal Count gr/24')),
                ('plasma_cells_in_bone_marrow', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Plasma Cells In Bone Marrow %')),
                ('freelite_count', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Freelite Count')),
                ('heavylite_count', models.FloatField(blank=True, max_length=256, null=True, verbose_name='Heavylite Count')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_mproteinmesurements_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_mproteinmesurements_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PatientOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('outcome_at_the_last_visit', models.CharField(blank=True, choices=[('Complete Response Molecular', 'Complete Response Molecular'), ('Complete Response Immunophenotypic', 'Complete Response Immunophenotypic'), ('Complete Response Strict', 'Complete Response Strict'), ('Very Good Partial Response', 'Very Good Partial Response'), ('Partial Response', 'Partial Response'), ('Stable Disease', 'Stable Disease'), ('Progression', 'Progression'), ('Unknown', 'Unknown'), ('Death', 'Death')], max_length=256, null=True, verbose_name='Outcome At The Last Visit')),
                ('status', models.CharField(blank=True, choices=[('Dead', 'Dead'), ('Lost', 'Lost'), ('Alive', 'Alive')], max_length=256, null=True, verbose_name='Status')),
                ('status_date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('cause_of_death', models.CharField(blank=True, choices=[('Multiple Myeloma', 'Multiple Myeloma'), ('Infection', 'Infection'), ('Thrombosis', 'Thrombosis'), ('Not Disease Related', 'Not Disease Related'), ('Not Available', 'not available'), ('Other', 'Other')], max_length=256, null=True, verbose_name='Cause Of Death')),
                ('cause_of_death_other', models.TextField(blank=True, default='', verbose_name='Other')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_patientoutcome_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient', verbose_name='Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_patientoutcome_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Patient Outcome',
                'verbose_name_plural': 'Patient Outcomes',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Radiotherapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='Updated')),
                ('consistency_token', models.CharField(max_length=8, verbose_name='Consistency Token')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_mm_radiotherapy_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode', verbose_name='Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_mm_radiotherapy_subrecords', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Radiotherapy',
                'verbose_name_plural': 'Radiotherapies',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='del_13',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='del_17p',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='diag_date',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='ds_stage',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='hospital_fk',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='hospital_ft',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='iss_stage',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='mgus_history',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='mgus_history_date',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='pp_type',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='smm_history',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='smm_history_date',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='t4_14',
        ),
        migrations.RemoveField(
            model_name='mmdiagnosisdetails',
            name='t4_16',
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='bone_pain_pres_clinic',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Pres Clinical Bone Pain'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='cc_scale',
            field=models.IntegerField(blank=True, null=True, verbose_name='ICC Scale'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='date_of_diagnosis',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Diagnosis'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='date_of_first_centre_visit',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of First Centre Visit'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='diagnosis',
            field=models.CharField(blank=True, choices=[('Solitary Bone Plasmacytoma', 'Solitary Bone Plasmacytoma'), ('Symptomatic Multiple Myeloma', 'Symptomatic Multiple Myeloma'), ('Plasmatic Celiac Leukemia', 'Plasmatic Celiac Leukemia'), ('Primary Amylodosis', 'Primary Amylodosis'), ('Asymptomatic MM', 'Asymptomatic MM')], max_length=256, null=True, verbose_name='Diagnosis'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='dialysis',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Dialysis'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='ecog',
            field=models.IntegerField(blank=True, null=True, verbose_name='ECOG'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='epidemiologic_registry',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Epidemiologic registry'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='extramedullary_plasmacytomas',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Extramedullary plasmacytomas'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='gah_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='GAH Score'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='height',
            field=models.IntegerField(blank=True, null=True, verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='imwg_scale',
            field=models.IntegerField(blank=True, null=True, verbose_name='IMWG Scale'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='infection_type',
            field=models.CharField(blank=True, choices=[('Clinically Documented Infection', 'Clinically Documented Infection'), ('Undocumented Infection', 'Undocumented Infection'), ('Microbiologically Documented Without Bacteremia', 'Microbiologically Documented Without Bacteremia'), ('Microbiologically Documented With Bacteremia', 'Microbiologically Documented With Bacteremia'), ('Other Microbiologic Documented Infection', 'Other Microbiologic Documented Infection')], max_length=256, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='ircp_diag_date',
            field=models.DateField(blank=True, null=True, verbose_name='IRCP Diagnosis Date'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='iss_diagnostic_status',
            field=models.CharField(blank=True, choices=[('One', 'One'), ('Two', 'Two'), ('Three', 'Three')], max_length=256, null=True, verbose_name='ISS Diagnostic Status'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='microorg_pc_focus',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='pres_clinical_anemia',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Pres Clinical Anemia'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='pres_clinical_description',
            field=models.TextField(blank=True, default='', verbose_name='Pres Clinical Description'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='pres_clinical_fever',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Pres Clinical Fever'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='pres_clinical_hypercalcemia',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Pres Clinical Hypercalcemia'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='pres_clinical_microorganism',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Pres Clinical Microorganism'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='pres_clinical_renal_failure',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Pres Clinical Renal Failure'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='previous_hospital',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Previous Hospital'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='referred',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Referred'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='riss_stage',
            field=models.CharField(blank=True, choices=[('Stage I', 'Stage I'), ('Stage II', 'Stage II'), ('Stage III', 'Stage III'), ('Unknown', 'Unknown')], max_length=256, null=True, verbose_name='R-ISS Stage'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='subclassification',
            field=models.CharField(blank=True, choices=[('MM IgG Kappa', 'MM IgG Kappa'), ('MM IgA Kappa', 'MM IgA Kappa'), ('MM IgD Kapper', 'MM IgD Kapper'), ('MM IgE Kapper', 'MM IgE Kapper'), ('MM Light Chain Kappa', 'MM Light Chain Kappa'), ('MM IgG Lambda', 'MM IgG Lambda'), ('MM IgA Lambda', 'MM IgA Lambda'), ('MM IgD Lambda', 'MM IgD Lambda'), ('MM IgE Lambda', 'MM IgE Lambda'), ('MM Light Chain Lambda', 'MM Light Chain Lambda'), ('Other', 'Other')], max_length=256, null=True, verbose_name='SUBCLASSIFICATION'),
        ),
        migrations.AddField(
            model_name='mmdiagnosisdetails',
            name='weight',
            field=models.FloatField(blank=True, max_length=256, null=True, verbose_name='Weight'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='comments',
            field=models.TextField(blank=True, default='', verbose_name='Comments'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='emr_technique',
            field=models.CharField(blank=True, choices=[('NGS', 'NGS'), ('FC (Flow Cytometry)', 'FC (Flow Cytometry)'), ('Both', 'Borth')], max_length=256, null=True, verbose_name='EMR2 Technique'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='negative_mrd',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Negative MRD'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='negative_mrd_date',
            field=models.DateField(blank=True, null=True, verbose_name='Negative MRD Date'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='regimen_description',
            field=models.TextField(blank=True, default='', verbose_name='Regimen Description'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='response_date',
            field=models.DateField(blank=True, null=True, verbose_name='Response Date'),
        ),
        migrations.AddField(
            model_name='mmregimen',
            name='stop_reason_description',
            field=models.TextField(blank=True, default='', verbose_name='Stop Reason Description'),
        ),
        migrations.AlterField(
            model_name='mmpastmedicalhistory',
            name='previous_neoplasm_2',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=256, null=True, verbose_name='Prevous Neoplasm 2'),
        ),
        migrations.AlterField(
            model_name='mmresponse',
            name='response_date',
            field=models.DateField(blank=True, null=True, verbose_name='Response Date'),
        ),
    ]
