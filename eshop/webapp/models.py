from django.db import models


category_choices = [('other', 'Other'), ('notebooks', 'Notebooks'), ('computers', 'Computers'), ('monitors', 'Monitors'), ('printers', 'Printers')]


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, verbose_name='Описание')
    category = models.CharField(max_length=30, null=False, choices=category_choices, default='other', verbose_name='Категория')
    count = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.name} - {self.category} - {self.price}'
