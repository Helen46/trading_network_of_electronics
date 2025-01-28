from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE


class Partner(models.Model):
    """Модель партнера"""
    TYPE_OF_PARTNER = [
        ('factory', 'завод'),
        ('retail chain', 'розничная сеть'),
        ('individual entrepreneur', 'индивидуальный предприниматель')
    ]
    type = models.CharField(
        max_length=23,
        choices=TYPE_OF_PARTNER,
        verbose_name='Тип партнера',
        help_text='Выберите тип партнера',
        default='retail chain',
    )
    name = models.CharField(
        max_length=300,
        verbose_name='Имя партнера',
        help_text='Введите имя организации или ИП',
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Владелец',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name


class PartnerContacts(models.Model):
    """Модель контактов партнера"""
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        verbose_name='Партнер',
        help_text='Укажите для какого партнера контакты'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта',
        help_text='Укажите электронную почту'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        help_text='Укажите страну'
    )
    city = models.CharField(
        max_length=200,
        verbose_name='Город',
        help_text='Укажите ваш город'
    )
    street = models.CharField(
        max_length=100,
        verbose_name='Улица',
        help_text='Укажите улицу'
    )
    building_number = models.CharField(
        max_length=10,
        verbose_name='Номер дома',
        help_text='Укажите номер дома'
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name='Владелец',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Контакты партнера'
        verbose_name_plural = 'Контакты партнеров'
