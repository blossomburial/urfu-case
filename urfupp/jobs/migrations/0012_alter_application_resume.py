# Generated by Django 5.1.2 on 2024-12-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_application_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
    ]