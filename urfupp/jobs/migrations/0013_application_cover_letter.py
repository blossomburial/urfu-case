# Generated by Django 5.1.2 on 2024-12-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_alter_application_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='cover_letter',
            field=models.TextField(default='', verbose_name='сопроводительно письмо'),
        ),
    ]