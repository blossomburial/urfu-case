from django.db import models
from django.contrib.auth.models import User


class Jobs(models.Model):
    type_of_jobs = [
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
        choices=type_of_jobs,
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
    
class UserProfile(models.Model):
    statuses = [
        ('active', 'активно ищу работу'),
        ('looking_for_offers', 'рассматриваю предложения'),
        ('disabled', 'не ищу'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField('о себе', blank=True, null=True)
    birth_date = models.DateField('дата рождения', null=True, blank=True)
    status = models.CharField('статус', choices=statuses, max_length=20, default='active')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True) 

    def __str__(self):
        return self.user.username
