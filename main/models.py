from django.db import models

class Person(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveIntegerField('Возраст')

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField('Текст')
    is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:40]
