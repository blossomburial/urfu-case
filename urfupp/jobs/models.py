from django.db import models


class Jobs(models.Model):
    title = models.CharField('название', max_length=50)
    desc = models.TextField('описание')
    type_of_job = models.CharField('тип работы', max_length=20)
    busyness = models.CharField('занятость', max_length=20)
    date = models.DateField('дата публикации', auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/jobs/{self.id}'
    
    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
