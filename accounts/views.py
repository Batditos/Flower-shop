
# from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from accounts.models import User
from basket.basket import Basket
from orders.models import Order, OrderItem
from django.views.generic.detail import DetailView


@login_required
def profile_views(request):
    basket = Basket(request)
    order_items = Order.objects.filter(
        user=request.user).order_by('-id')
    # order_items = Order.objects.filter(order_id=)
    assert isinstance(request, HttpRequest)
    context = {
        "basket": basket,
        "order_items": order_items
    }
    return render(request, 'account/profile.html', context)


class OrderViews(DetailView):
    model = Order
    template_name = 'account/orderview.html'


class UpdateProfile(UpdateView):
    model = User
    template_name = 'account/updateprofile.html'
    fields = ['image_user', 'first_name', 'last_name', 'email', 'phone_number']
    labels = {'email': '1111'}


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(17)
            cd = form.cleaned_data
            user = authenticate(
                email=cd['email'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_staff == True:
                        return redirect('adminpanel:admin')
                    else:

                        return redirect('accounts:profile_views')

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):

    print('line 41')
    form = LoginForm(request.POST)
    if request.method == 'POST':
        print('line 43')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('line 46')
            form.save()
            print('save')
            cd = form.cleaned_data
            user = authenticate(
                email=cd['email'], password=cd['password1'])

            if user is not None:
                if user.is_active:
                    login(request, user)
            return render(request, 'account/profile.html', {'form': form})
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_views(request):
    logout(request)
    return redirect('accounts:user_login')

# def my_orders(request):
#     order_items = Order.objects.filter(user=request.user)
#     # order_items = Order.objects.all()
#     print(order_items)
#     assert isinstance(request, HttpRequest)
#     return render(request, 'account/profile.html', {'order_items': order_items,})

# @login_required
# @transaction.atomic


# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, gettext_lazy(
#                 'Ваш профиль успешно обновлен!'))
#             return redirect('accounts:profile_views')
#         else:
#             messages.error(request, gettext_lazy(
#                 'Пожалуйста, исправьте ошибку ниже.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'account/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
