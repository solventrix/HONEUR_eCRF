# Generated by Django 2.2.16 on 2022-08-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0002_mmstemcelltransplanteligibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='del_13',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='del13'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='del_17p',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='del(17)p'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='ds_stage',
            field=models.CharField(blank=True, choices=[('Stage I', 'Stage I'), ('Stage II', 'Stage II'), ('Stage III', 'Stage III'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='DS Stage'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='iss_stage',
            field=models.CharField(blank=True, choices=[('Stage I', 'Stage I'), ('Stage II', 'Stage II'), ('Stage III', 'Stage III'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='ISS Stage'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='mgus_history',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='History of MGUS'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='pp_type',
            field=models.CharField(blank=True, choices=[('IgG', 'IgG'), ('IgA', 'IgA'), ('IgE', 'IgE'), ('Light Chain Myeloma', 'Light Chain Myeloma')], max_length=50, null=True, verbose_name='PP Type'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='smm_history',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='History of SMM'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='t4_14',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='t(4;14)'),
        ),
        migrations.AlterField(
            model_name='mmdiagnosisdetails',
            name='t4_16',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Unknown', 'Unknown')], max_length=10, null=True, verbose_name='t(4;16)'),
        ),
        migrations.AlterField(
            model_name='mmfollowup',
            name='follow_up_date',
            field=models.DateField(blank=True, null=True, verbose_name='Visit date'),
        ),
        migrations.AlterField(
            model_name='mmregimen',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='mmresponse',
            name='response',
            field=models.CharField(blank=True, choices=[('Minimal response', 'Minimal response'), ('Partial response', 'Partial response'), ('Very good partial response', 'Very good partial response'), ('Complete response', 'Complete response'), ('Stringent complete response', 'Stringent complete response'), ('Near complete response', 'Near complete response'), ('Immunophenotypic complete response', 'Immunophenotypic complete response'), ('Stable disease', 'Stable disease'), ('Progressive disease', 'Progressive disease'), ('Response unknown/NA', 'Response unknown/NA')], max_length=50, null=True, verbose_name='Response'),
        ),
        migrations.AlterField(
            model_name='mmresponse',
            name='response_date',
            field=models.DateField(blank=True, null=True, verbose_name='Response Date'),
        ),
    ]
