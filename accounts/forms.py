
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField, formfields
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(forms.ModelForm):
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):

    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Введите Email', 'class': 'username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'placeholder': 'Введите пароль'}))

    def clean(self):
        self.cd = super(LoginForm, self).clean()
        email = self.cd['email']
        password = self.cd['password']

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Пользователь с такой почтой не зарегистрирован')

        user = User.objects.get(email=email)
        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')




class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'email', 'phone_number')
        
    email = forms.EmailField(label='Email')
    # username = forms.CharField(label='Логин', min_length=5, max_length=150)
    first_name = forms.CharField(label='Имя', min_length=2,)
    # last_name = forms.CharField(label='Фамилия')
    phone_number = formfields.PhoneNumberField()

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput)

    def username_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Пользователь уже существует")
        return email


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(
                "Пользователь с такой электронной зарегистрирован")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароль не подходит")
        return password2
