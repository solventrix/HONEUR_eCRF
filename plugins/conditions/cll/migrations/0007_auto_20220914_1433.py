# Generated by Django 2.2.16 on 2022-09-14 14:33

from django.db import migrations, models


TRANSLATION_MAPPING = {
    "CR": "Complete Remission",
    "PD": "Progressive Disease",
    "PR": "Partial Response",
    "SD": "Stable Disease",
}


def forwards(apps, schema_editor):
    BestResponse = apps.get_model(
        'cll', 'BestResponse'
    )
    for old, new in TRANSLATION_MAPPING.items():
        BestResponse.objects.filter(
            response=old
        ).update(
            response=new
        )


def backwards(apps, schema_editor):
    BestResponse = apps.get_model(
        'cll', 'BestResponse'
    )
    for old, new in TRANSLATION_MAPPING.items():
        BestResponse.objects.filter(
            response=new
        ).update(
            response=old
        )


class Migration(migrations.Migration):

    dependencies = [
        ('cll', '0006_auto_20220218_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestresponse',
            name='response',
            field=models.CharField(choices=[('Complete Remission', 'Complete Remission'), ('Progressive Disease', 'Progressive Disease'), ('Partial Response', 'Partial Response'), ('Stable Disease', 'Stable Disease'), ('Unknown', 'Unknown')], max_length=50, verbose_name='Best Response'),
        ),
        migrations.RunPython(forwards, reverse_code=backwards),
    ]
