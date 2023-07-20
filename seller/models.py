from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(max_length=50, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    purchase_status = models.BooleanField(default=False, verbose_name='Статус покупки')
    purchase_date = models.DateField(null=True, blank=True, verbose_name='Дата покупки')
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
