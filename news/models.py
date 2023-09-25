from django.db import models


class Tasks(models.Model):    #поля формы
    number = models.IntegerField('Номер задачи', default=0)
    title = models.CharField('Название задачи', max_length=50)
    text = models.CharField('Описание задачи', max_length=250)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
