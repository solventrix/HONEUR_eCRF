# Generated by Django 2.0.13 on 2020-04-02 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0038_auto_20191206_1449'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entrytool', '0011_auto_20200402_0957'),
    ]

    operations = [
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
        migrations.RemoveField(
            model_name='regimen',
            name='lot',
        ),
        migrations.AddField(
            model_name='regimen',
            name='lot_ft',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='regimen',
            name='lot_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='entrytool.TreatmentLine'),
        ),
    ]
