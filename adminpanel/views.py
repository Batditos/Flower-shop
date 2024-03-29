
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,  CreateView, DeleteView
from django.views.generic.detail import DetailView
from accounts.models import User
from adminpanel.forms import UpdateProductForm
from orders.models import Order, OrderItem
from shop.models import Product
from accounts.models import User
from accounts.forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin


def admin(request):
    users = User.objects.all()
    order = Order.objects.all()
    products = Product.objects.all()
    len_users = len(users)
    len_orders = len(order)
    context = {
        'users': users,
        'products': products,
        'len_users': len_users,
        'len_orders': len_orders
    }
    return render(request, 'adminpanel/admin.html', context)


# def orders(request):
#     context = {}
#     return render(request, 'adminpanel/orders.html', context)


def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'adminpanel/user/users.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'adminpanel/product/products.html/', context)


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'adminpanel/product/updateproduct.html/'
    fields = ['image', 'name', 'price', 'quantity', 'category', 'description']


class AddProduct(CreateView):
    model = Product
    template_name = 'adminpanel/product/addproduct.html/'
    fields = ['image', 'name', 'price', 'quantity', 'category', 'description']


class DelProduct(DeleteView):
    model = Product
    template_name = 'adminpanel/product/delproduct.html/'
    success_url = reverse_lazy('adminpanel:products')

class OrderViews(DetailView):
    model = Order
    template_name = 'adminpanel/order/list_orders.html/'

def orders(request):
    orders= Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'adminpanel/order/orders.html', context)
class UpdateOrder(UpdateView):
    model = Order
    template_name = 'adminpanel/order/updateorder.html/'
    fields = ['status']
    