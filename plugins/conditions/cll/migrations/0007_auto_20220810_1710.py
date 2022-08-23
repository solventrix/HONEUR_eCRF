# Generated by Django 2.2.16 on 2022-08-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cll', '0006_auto_20220218_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalcharacteristics',
            name='characteristic_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of measurement'),
        ),
        migrations.AlterField(
            model_name='clldiagnosisdetails',
            name='binet_stage',
            field=models.CharField(blank=True, choices=[('Stage A', 'Stage A'), ('Stage B', 'Stage B'), ('Stage C', 'Stage C'), ('Unknown', 'Unknown')], max_length=100, null=True, verbose_name='Binet Stage'),
        ),
        migrations.AlterField(
            model_name='cllregimen',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='cytogenetics',
            name='cytogenetic_date',
            field=models.DateField(blank=True, null=True, verbose_name='Cytogenetic Date'),
        ),
        migrations.AlterField(
            model_name='qualityoflife5q',
            name='q5_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Questionnaire'),
        ),
    ]
