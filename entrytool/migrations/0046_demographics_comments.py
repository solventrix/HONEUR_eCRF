# Generated by Django 2.0.13 on 2022-04-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrytool', '0045_auto_20220224_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographics',
            name='comments',
            field=models.TextField(blank=True, default='', verbose_name='Comments'),
        ),
    ]