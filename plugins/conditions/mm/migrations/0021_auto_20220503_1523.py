# Generated by Django 2.2.16 on 2022-05-03 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0020_delete_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comorbidity',
            options={'verbose_name': 'Comorbidities', 'verbose_name_plural': 'Comorbidities'},
        ),
        migrations.AlterModelOptions(
            name='labtest',
            options={'verbose_name': 'Lab Tests', 'verbose_name_plural': 'Lab Tests'},
        ),
    ]
