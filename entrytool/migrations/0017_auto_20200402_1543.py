# Generated by Django 2.0.13 on 2020-04-02 13:43

from django.db import migrations, models
import entrytool.models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0016_auto_20200402_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regimen',
            name='start_date',
            field=models.DateField(validators=[entrytool.models.validate_emptystring], verbose_name='Start Date'),
        ),
    ]
