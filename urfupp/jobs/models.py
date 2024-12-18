from django.db import models


class Jobs(models.Model):
    TYPE_OF_JOB_CHOICES = [
        ('full_time', 'полная занятость'),
        ('part_time', 'частичная занятость'),
        ('remote', 'удалённая работа'),
        ('intern', 'стажировка')
    ]

    title = models.CharField('название', max_length=50)
    desc = models.TextField('описание')
    type_of_job = models.CharField(
        'тип работы',
        max_length=20,
        choices=TYPE_OF_JOB_CHOICES,
        default='full_time'
    )
    date = models.DateField('дата публикации', auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/jobs/{self.id}'
    
    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
