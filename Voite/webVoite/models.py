from django.db import models
from .forms import *
from django.contrib.auth.models import User
from django.contrib import admin

Select_floor = [
    ('B', 'Мальчик'),
    ('G', 'Девочка')
]


class Person(models.Model):
    IP = models.CharField(max_length=20)
    Name = models.CharField(max_length=30)
    floor = models.CharField(max_length=20,blank=True,choices=Select_floor)

    def __str__(self):
        return self.Name

admin.site.register(Person)