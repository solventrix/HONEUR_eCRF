# Generated by Django 2.2.16 on 2022-09-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0012_merge_20220915_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmresponse',
            name='response_date',
            field=models.DateField(verbose_name='Response Date'),
        ),
    ]
