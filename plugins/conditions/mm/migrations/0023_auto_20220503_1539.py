# Generated by Django 2.2.16 on 2022-05-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm', '0022_auto_20220503_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonedisease',
            name='treatment_type',
            field=models.CharField(blank=True, choices=[('Denosumab', 'Denosumab'), ('Bisphosphonates Induction', 'Bisphosphonates Induction'), ('Vertebroplasty Induction', 'Vertebroplasty Induction'), ('Other Induction', 'Other Induction'), ('Not Available', 'Not Available')], max_length=256, null=True, verbose_name='Treatment Type'),
        ),
    ]