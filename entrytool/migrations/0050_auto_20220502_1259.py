# Generated by Django 2.2.16 on 2022-05-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0049_auto_20220428_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sct',
            name='sct_type',
            field=models.CharField(choices=[('Allogenic', 'Allogenic'), ('Autologous', 'Autologous'), ('Tandem ATSP', 'Tandem ATSP'), ('Unknown', 'Unknown')], max_length=12, null=True, verbose_name='Type of SCT'),
        ),
    ]
