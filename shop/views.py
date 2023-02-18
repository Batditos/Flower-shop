from django.shortcuts import render
from shop.models import Product

def index(request):
    context = {
        'product': Product.objects.all()
    }
    return render(request, 'shop/main.html', context)
