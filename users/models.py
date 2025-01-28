from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE
from partners.models import Partner


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
        help_text='Укажите вашу электронную почту'
    )
    first_name = models.CharField(
        max_length=50,
        **NULLABLE,
        verbose_name='Имя пользователя',
        help_text='Укажите имя'
    )
    last_name = models.CharField(
        max_length=150,
        **NULLABLE,
        verbose_name='Фамилия пользователя',
        help_text='Укажите фамилию'
    )
    phone = models.CharField(
        max_length=35,
        **NULLABLE,
        verbose_name='Номер телефона',
        help_text='Укажите ваш номер телефона'
    )
    country = models.CharField(
        max_length=100,
        **NULLABLE,
        verbose_name='Страна',
        help_text='Укажите вашу страну'
    )
    city = models.CharField(
        max_length=200,
        **NULLABLE,
        verbose_name='Город',
        help_text='Укажите ваш город'
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        **NULLABLE,
        verbose_name='Аватар',
        help_text='Загрузите аватар'
    )
    place_of_work = models.ForeignKey(
        Partner,
        on_delete=models.SET_NULL,
        verbose_name='Место работы',
        help_text='Укажите ИП или организацию сотрудником, которой вы являетесь',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'