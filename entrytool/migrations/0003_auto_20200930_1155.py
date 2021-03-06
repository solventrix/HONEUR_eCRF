# Generated by Django 2.0.13 on 2020-09-30 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0002_diagnosis_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
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
        migrations.AddField(
            model_name='followup',
            name='hospital_ft',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='regimen',
            name='hospital_ft',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sct',
            name='hospital_ft',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='hospital',
            unique_together={('code', 'system')},
        ),
        migrations.AddField(
            model_name='followup',
            name='hospital_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.Hospital'),
        ),
        migrations.AddField(
            model_name='regimen',
            name='hospital_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.Hospital'),
        ),
        migrations.AddField(
            model_name='sct',
            name='hospital_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.Hospital'),
        ),
    ]
