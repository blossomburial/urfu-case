# Generated by Django 5.1.2 on 2024-12-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_jobs_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(max_length=20, verbose_name='заработная плата'),
        ),
    ]
