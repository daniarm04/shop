from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

COUNTRY_CHOICES = [
        ('Россия', 'Россия'),
        ('США', 'США'),
        ('Великобритания', 'Великобритания'),
        ('Франция', 'Франция'),
]


class User(AbstractUser):
    country = models.CharField(blank=True, max_length=100, verbose_name='Страна',  choices=COUNTRY_CHOICES)

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
