# Generated by Django 2.0.13 on 2022-02-16 10:08
"""
As part of moving the project from a single condition
to multiple conditions we need to move all the
existing 'Default' episdoe categories to
'CLL' episode categories
"""

from django.db import migrations


def forwards(apps, schema_editor):
    Episode = apps.get_model('opal', 'episode')
    Episode.objects.filter(category_name='Default').update(category_name='CLL')


def backwards(apps, schema_editor):
    Episode = apps.get_model('opal', 'episode')
    Episode.objects.filter(category_name='CLL').update(category_name='Default')


class Migration(migrations.Migration):

    dependencies = [
        ('cll', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            forwards, backwards
        )
    ]
