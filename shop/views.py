from django.shortcuts import get_object_or_404, render
from basket.basket import Basket
from shop.models import Product
from basket.forms import CartAddProductForm

def index(request):
    basket = Basket(request)
    context = {
        'products': Product.objects.all(),
        "baskets": basket
    }
    return render(request, 'shop/main.html', context)

def catalog(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop/catalog.html', context)

# def len_basket(request):
#     basket = Basket(request)
#     context = {
#         "baskets": basket
#     }
#     return render(request, 'shop/main.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/catalog.html', {'product': product,
                                                        'cart_product_form': cart_product_form})