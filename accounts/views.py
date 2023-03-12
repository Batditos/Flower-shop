
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(17)
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'], password=cd['password'])
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
    return render(request, 'account/profile.html')


def register(request):
    print('line 41')
    if request.method == 'POST':
        print('line 43')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('line 46')
            form.save()
            return redirect('accounts:profile_views')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
