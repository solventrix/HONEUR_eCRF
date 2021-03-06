# Generated by Django 2.0.13 on 2020-10-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0016_auto_20201007_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adverseevent',
            options={'verbose_name': 'Adverse Event', 'verbose_name_plural': 'Adverse Event'},
        ),
        migrations.AlterModelOptions(
            name='aelist',
            options={'verbose_name': 'AE List', 'verbose_name_plural': 'AE List'},
        ),
        migrations.AlterModelOptions(
            name='followup',
            options={'verbose_name': 'Follow-up', 'verbose_name_plural': 'Follow-ups'},
        ),
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name': 'Hospital', 'verbose_name_plural': 'Hospitals'},
        ),
        migrations.AlterModelOptions(
            name='patientdetails',
            options={'verbose_name': 'Patient Details', 'verbose_name_plural': 'Patient Details'},
        ),
        migrations.AlterModelOptions(
            name='regimen',
            options={'verbose_name': 'Regimen', 'verbose_name_plural': 'Regimens'},
        ),
        migrations.AlterModelOptions(
            name='regimenlist',
            options={'verbose_name': 'Regimen List', 'verbose_name_plural': 'Regimen List'},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'Response', 'verbose_name_plural': 'Responses'},
        ),
        migrations.AlterModelOptions(
            name='stopreason',
            options={'verbose_name': 'Stop Reason', 'verbose_name_plural': 'Stop Reason'},
        ),
        migrations.AlterModelOptions(
            name='treatmentline',
            options={'verbose_name': 'Treatment Line', 'verbose_name_plural': 'Treatment Lines'},
        ),
        migrations.AlterField(
            model_name='response',
            name='response',
            field=models.CharField(choices=[('Minimal response', 'Minimal response'), ('Partial response', 'Partial response'), ('Very good partial response', 'Very good partial response'), ('Complete response', 'Complete response'), ('Stringent complete response', 'Stringent complete response'), ('Near complete response', 'Near complete response'), ('Immunophenotypic complete response', 'Immunophenotypic complete response'), ('Stable disease', 'Stable disease'), ('Progressive disease', 'Progressive disease'), ('Response unknown', 'Response unknown')], max_length=50, verbose_name='Response'),
        ),
        migrations.AlterUniqueTogether(
            name='aelist',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='hospital',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='regimenlist',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='stopreason',
            unique_together=set(),
        ),
    ]
