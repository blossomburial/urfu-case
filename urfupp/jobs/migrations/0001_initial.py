# Generated by Django 5.1.2 on 2024-12-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('desc', models.TextField(verbose_name='описание')),
                ('type_of_job', models.CharField(max_length=20, verbose_name='тип работы')),
                ('busyness', models.CharField(max_length=20, verbose_name='занятость')),
            ],
        ),
    ]