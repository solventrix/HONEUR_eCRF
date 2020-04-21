# Generated by Django 2.0.13 on 2020-04-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0038_auto_20191206_1449'),
        ('entrytool', '0027_remove_regimen_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='opal.Patient')),
            ],
            bases=('opal.patient',),
        ),
    ]
