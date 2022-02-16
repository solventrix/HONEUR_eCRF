# Generated by Django 2.0.13 on 2022-02-16 10:08
"""
As part of moving the project from a single indication
to multiple indications we need to move all the
existing 'default' episdoe categories to
'cll base' episode categories
"""

from django.db import migrations


def forwards(apps, schema_editor):
    Episode = apps.get_model('opal', 'episode')
    Episode.objects.filter(category_name='Default').update(category_name='CLL Base')


def backwards(apps, schema_editor):
    Episode = apps.get_model('opal', 'episode')
    Episode.objects.filter(category_name='CLL Base').update(category_name='Default')


class Migration(migrations.Migration):

    dependencies = [
        ('cll', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            forwards, backwards
        )
    ]