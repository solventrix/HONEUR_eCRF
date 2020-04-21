# Generated by Django 2.0.13 on 2020-03-31 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0038_auto_20191206_1449'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entrytool', '0003_auto_20200331_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('diag_date', models.DateField()),
                ('smm_history', models.CharField(max_length=10)),
                ('smm_history_date', models.DateField()),
                ('mgus_history', models.DateField()),
                ('r_iss_stage', models.CharField(max_length=10)),
                ('pp_type', models.CharField(max_length=50)),
                ('del_17p', models.CharField(max_length=10)),
                ('t4_14', models.CharField(max_length=10)),
                ('t4_16', models.CharField(max_length=10)),
                ('death_date', models.DateField()),
                ('death_cause', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_entrytool_patientdetails_subrecords', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Patient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_entrytool_patientdetails_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='sct',
            options={'verbose_name': 'Stem Cell Transplant', 'verbose_name_plural': 'Stem Cell Transplants'},
        ),
    ]
