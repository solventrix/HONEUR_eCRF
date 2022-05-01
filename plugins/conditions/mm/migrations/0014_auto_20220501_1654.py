# Generated by Django 2.2.16 on 2022-05-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0013_auto_20220501_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmregimen',
            name='start_reason',
            field=models.CharField(blank=True, choices=[('Progression', 'Progression'), ('Clinical Relapse', 'Clinical Relapse'), ('Biological Relapse', 'Biological Relapse'), ('Other', 'Other')], max_length=256, null=True, verbose_name='Start Reason'),
        ),
    ]
