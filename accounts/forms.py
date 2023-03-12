from django.forms.forms import Form
from django.forms.fields import EmailField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'placeholder': 'Введите логин', 'class': 'username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'placeholder': 'Введите пароль'}))

    def clean(self):
        self.cd = super(LoginForm, self).clean()
        username = self.cd['username']
        password = self.cd['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Пользователь с таким логином не зарегистрирован')

        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', min_length=5, max_length=150)
    # first_name = forms.CharField(label='Имя')
    # last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Пользователь уже существует")
        return username
    

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Пользователь с такой электронной зарегистрирован")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароль не подходит")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            # self.cleaned_data['first_name'],
            # self.cleaned_data['last_name'],
        )
        print('сохранил')
        return user
