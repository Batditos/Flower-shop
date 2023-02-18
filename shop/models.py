from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='static/media')
    category = models.CharField(default='', max_length=21, unique=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')

    def __str__(sefl):
        return sefl.name
