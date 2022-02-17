# Generated by Django 2.0.13 on 2022-02-17 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0043_auto_20210914_1147'),
        ('cll', '0005_copy_model_instances_into_cll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalcharacteristics',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='additionalcharacteristics',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='additionalcharacteristics',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='cytogenetics',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='cytogenetics',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='cytogenetics',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='hospital_fk',
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patientdetails',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='qualityoflife5q',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='qualityoflife5q',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='qualityoflife5q',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='hospital_fk',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='regimen_fk',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='stop_reason_fk',
        ),
        migrations.RemoveField(
            model_name='regimen',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='response',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='response',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='response',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='AdditionalCharacteristics',
        ),
        migrations.DeleteModel(
            name='Cytogenetics',
        ),
        migrations.DeleteModel(
            name='PatientDetails',
        ),
        migrations.DeleteModel(
            name='QualityOfLife5Q',
        ),
        migrations.DeleteModel(
            name='Regimen',
        ),
        migrations.DeleteModel(
            name='RegimenList',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.DeleteModel(
            name='StopReason',
        ),
    ]
