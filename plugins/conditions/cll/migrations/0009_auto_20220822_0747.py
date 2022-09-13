# Generated by Django 2.2.16 on 2022-08-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cll', '0008_auto_20220811_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualityoflife5q',
            name='q5_anxiety_depression',
            field=models.FloatField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True, verbose_name='Anxiety/Depression'),
        ),
        migrations.AlterField(
            model_name='qualityoflife5q',
            name='q5_mobility',
            field=models.FloatField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True, verbose_name='Mobility'),
        ),
        migrations.AlterField(
            model_name='qualityoflife5q',
            name='q5_pain_discomfort',
            field=models.FloatField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True, verbose_name='Pain/Discomfort'),
        ),
        migrations.AlterField(
            model_name='qualityoflife5q',
            name='q5_selfcare',
            field=models.FloatField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True, verbose_name='Selfcare'),
        ),
        migrations.AlterField(
            model_name='qualityoflife5q',
            name='q5_usual_activities',
            field=models.FloatField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True, verbose_name='Usual Activities'),
        ),
    ]