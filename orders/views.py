from basket.basket import Basket
from .forms import OrderCreateForm
from .models import Order, OrderItem
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.views import View

from accounts.models import User
from shop.models import Product


# def main(request):
#     context = {}
#     return render(request, 'orders/order.html', context)


def order_create(request):
    
    cart = Basket(request)
    if request.method == 'POST':
        user = request.user
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.final_price = cart.get_total_price()
            order.user = request.user
            order.save()
            order = form.save()
            for item in cart:
                order_item = OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
                products = Product.objects.get(id=order_item.product.id)
                products.quantity = products.quantity - order_item.quantity
                products.save()
            cart.clear()
            return redirect('accounts:profile_views')

    else:
        form = OrderCreateForm()
    return render(request, 'orders/order.html',
                  {'cart': cart, 'form': form})
# def order_create(request):
#     cart = Basket(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()

#             # очистка корзины
#             cart.clear()
#             return render(request, 'account/profile.html/',
#                           {'order': order})
#     else:
#         form = OrderCreateForm
#     return render(request, 'orders/order.html',
#                   {'cart': cart, 'form': form})
