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
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        help_text='Укажите поставщика',
        null=True
    )
    email = models.EmailField(
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
    created_at = models.DateTimeField(
        verbose_name="Дата создания (записи в БД)",
        auto_now_add=True
    )
    amount_credit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Задолженность перед поставщиком'
    )

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """Модель продукта"""
    owner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=300,
        verbose_name='Название продукта',
        help_text='Введите название продукта'
    )
    model = models.CharField(
        max_length=150,
        verbose_name='Модель продукта',
        help_text='Введите модель продукта',
        **NULLABLE
    )
    launch_date = models.DateField(
        verbose_name='Дата выхода продукта на рынок',
        help_text='Введите дату выхода продукта на рынок в формате ГГГГ-ММ-ДД'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'
