# Generated by Django 5.1.2 on 2024-12-17 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
        migrations.AddField(
            model_name='jobs',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='дата публикации'),
        ),
    ]