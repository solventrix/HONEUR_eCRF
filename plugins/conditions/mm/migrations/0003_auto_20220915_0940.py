# Generated by Django 2.2.16 on 2022-09-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0002_mmpastmedicalhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmfollowup',
            name='mprotein_24h',
            field=models.FloatField(blank=True, null=True, verbose_name='Mprotein In 24 Hour Urine'),
        ),
    ]
