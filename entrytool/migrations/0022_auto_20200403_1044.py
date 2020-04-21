# Generated by Django 2.0.13 on 2020-04-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0021_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='hospital',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='regimen',
            name='lot',
            field=models.IntegerField(verbose_name='Line of Treatment'),
        ),
    ]
