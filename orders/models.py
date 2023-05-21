from django.db import models
from accounts.models import User
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal

ORDER_STATUS = {
     ('Передан курьеру', 'Передан курьеру'),
      ('Выполнен', 'Выполнен'),
    ('Принят', 'Принят'),
   
   
}

class Order(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Покупатель')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50)
    phone = PhoneNumberField(unique=False,  verbose_name='Номер телефона')
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name='Адрес')
    delivery_type = models.CharField(blank=True, max_length=40, choices=(('Самовывоз', 'Самовывоз'), ('Доставкаy', 'Доставка')), verbose_name='Тип доставки', default='Самовывоз')
    comments = models.TextField(blank=True, verbose_name='Комментарий к заказу', default='')
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Новый заказ', verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    final_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Итоговая сумма')
    
    lables = {
            'last_name': '1111'
        }
    
    def __str__(self):
        return {self.user.email}

    class Meta:
        ordering = ('-created',)

        

    def get_absolute_url(self):
        return f'/adminpanel/orders/'


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Заказ товаров', related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f" # {self.order.id} {self.order.user}: {self.product.name}"

    
    def get_cost(self):
        return self.price * self.quantity

