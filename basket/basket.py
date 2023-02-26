from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Basket(object):

    def __init__(self, request):
        """Инициализируем корзину"""

        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:

            basket = self.session[settings.CART_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, quantity=1, update_quantity=False):
        """Добавления товара в корзину"""

        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 0,
                                       'price': str(product.price)}
        if update_quantity:

            self.basket[product_id]['quantity'] = quantity

        else:
            self.basket[product_id]['quantity'] += quantity
            print(self.basket[product_id]['quantity'])
        self.save()

    def save(self):
        # Обновление сессии basket
        self.session[settings.CART_SESSION_ID] = self.basket
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """Удаление товара из корзины."""

        product_id = str(product.id)
        if product_id in self.basket:
            print(self.basket)
            print('удаление',product_id)
            del self.basket[product_id]
        self.save()

    def __iter__(self):

        product_ids = self.basket.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.basket[str(product.id)]['product'] = product
            # print('55 views', self.basket[str(product.id)])  # TODO

        for item in self.basket.values():

            item['price'] = Decimal(item['price'])
            # Получение общей стоимости товаров одного типа
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def minus(self, product):
        '''Уменьшение товара в корзине'''

        # product_ids = self.basket.keys()
        # print(70, product_ids)
        # products = Product.objects.filter(id__in=product_ids)
        product_id = str(product.id)
        if product_id in self.basket:
            quantity = self.basket[str(product.id)]['quantity']
            if quantity > 1:
                    print(quantity)
                    self.basket[str(product.id)]['quantity'] -= 1
        self.save()
        return self.basket[str(product.id)]['quantity']
    

    def plus(self, product):
        '''Увиличения товара в корзине'''

        product_id = str(product.id)
        if product_id in self.basket:
            quantity = self.basket[str(product.id)]['quantity']
            if quantity >= 1:
                    print(quantity)
                    self.basket[str(product.id)]['quantity'] += 1
        self.save()
        return self.basket[str(product.id)]['quantity']


    def len(self):
        """Получение общего кол-во товаров в корзине"""
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        """Получение общей сумму товаров в корзине"""

        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.basket.values())

    def clear(self):
        """Очистка сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
