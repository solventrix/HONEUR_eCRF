# Generated by Django 2.0.13 on 2020-10-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0008_regimen_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regimen',
            name='category',
            field=models.CharField(choices=[('Induction', 'Induction'), ('Maintenance', 'Maintenance'), ('Conditioning', 'Conditioning'), ('Watch and wait', 'Watch and wait')], max_length=40, verbose_name='Regimen Type'),
        ),
    ]
