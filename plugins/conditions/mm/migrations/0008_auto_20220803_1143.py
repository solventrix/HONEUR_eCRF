# Generated by Django 2.0.13 on 2022-08-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0007_auto_20220803_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labtest',
            name='creatinine',
            field=models.FloatField(blank=True, max_length=256, null=True, verbose_name='Creatinine Clearance'),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='kappa_light_chain_count',
            field=models.FloatField(blank=True, max_length=256, null=True, verbose_name='Kappa Count'),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='lambda_light_chain_count',
            field=models.FloatField(blank=True, max_length=256, null=True, verbose_name='Lambda Count'),
        ),
        migrations.AlterField(
            model_name='labtest',
            name='mprotein_24h',
            field=models.FloatField(blank=True, null=True, verbose_name='Mprotein in 24 hour'),
        ),
    ]
