
# from django.db import transaction
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from basket.basket import Basket


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
                    return redirect('accounts:profile_views')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_views(request):
    logout(request)
    return redirect('accounts:user_login')


@login_required
def profile_views(request):
    basket = Basket(request)
    context = {
        "baskets": basket
    }
    return render(request, 'account/profile.html', context)


def register(request):

    print('line 41')
    form = LoginForm(request.POST)
    if request.method == 'POST':
        print('line 43')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('line 46')
            form.save()
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

