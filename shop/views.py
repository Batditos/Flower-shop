from django.shortcuts import get_object_or_404, render
from basket.basket import Basket
from shop.models import Product
from basket.forms import CartAddProductForm
from django.views.generic.detail import DetailView
from django.db.models import Q

def index(request):
    basket = Basket(request)
    context = {
        'products': Product.objects.all(),
        "baskets": basket
    }
    return render(request, 'shop/main.html', context)

def catalog(request):
    search = request.POST.get('search', '')
    if search:
        products = Product.objects.filter(Q(name__icontains=search) | Q(category__icontains=search))
    else:
        products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/catalog.html', context)

def len_basket(request):
    basket = Basket(request)
    context = {
        "baskets": basket
    }
    return render(request, 'shop/main.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/catalog.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

class ProductView(DetailView):
    model = Product
    template_name = 'shop/detailproduct.html'


    