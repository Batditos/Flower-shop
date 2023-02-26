from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .basket import Basket
from .forms import CartAddProductForm


def plus_quantity(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.plus(product)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def minus_quantity(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.minus(product)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print('18')
    if not form.is_valid():
        cd = form.cleaned_data
        print('строчка 20', cd)
        basket.add(product=product,
                   quantity=1,
                   update_quantity=cd['update'])
    # return redirect('basket:basket_detail')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket:basket_detail')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})
