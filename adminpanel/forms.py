

from django import forms

from shop.models import Product
from accounts.models import User

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

