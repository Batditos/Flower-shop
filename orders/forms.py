from django import forms
from phonenumbers import PhoneNumber
from .models import Order
from phonenumber_field.modelfields import PhoneNumberField

class OrderCreateForm(forms.ModelForm):
 

    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                    'phone', 'address', 'delivery_type', 'comments']
        # fields = ['first_name', 'email']
        labels = {
    'first_name': '',
    'last_name': '',
    'phone': '',
    'address': '',
    'comments': ''

}
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}),
            'address': forms.TextInput(attrs={'placeholder': 'Введите адрес'}),
            'comments': forms.Textarea(attrs={'placeholder': 'Комментарий к заказу'}),
        }