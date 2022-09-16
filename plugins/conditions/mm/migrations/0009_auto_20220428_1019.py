# Generated by Django 2.0.13 on 2022-04-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0008_auto_20220428_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mmpastmedicalhistory',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='mmpastmedicalhistory',
            name='previous_neoplasm_2',
        ),
        migrations.AddField(
            model_name='mmpastmedicalhistory',
            name='gmp_comments',
            field=models.TextField(blank=True, default='', verbose_name='GMP Comments'),
        ),
    ]