from django.db import models
# from django.contrib.auth.models import User


class Product(models.Model):
    image = models.ImageField(upload_to='media', verbose_name='Фото')
    category = models.CharField(default='', max_length=21, unique=True, verbose_name='Категории')
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    price = models.DecimalField(max_digits=8, decimal_places=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    description = models.TextField(default='', verbose_name='Описание')

    def __str__(sefl):
        return sefl.name
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    def get_absolute_url(self):
        return f'/adminpanel/products/'
