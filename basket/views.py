from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .basket import Basket
from .forms import CartAddProductForm


@require_POST
def basket_add(request, product_id):

    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if not form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                   quantity=['quantity'],
                   update_quantity=['update'])
    return redirect('basket:basket_detail')
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket:basket_detail')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})
