
from django.db import models


class Application(models.Model):
    title = models.CharField(null=True, default="", max_length=255)
    description = models.TextField(verbose_name='Текст заявки', default="")
    number = models.CharField(max_length=12, verbose_name='Номер заявщика', default="")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')
    last_activity = models.DateTimeField(auto_now_add=True)
    start_work = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    person = models.TextField(default="")
    executor = models.TextField(default="")
    status = models.TextField(default="")
    tags = models.TextField(default="")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"Заявка {self.number}"
