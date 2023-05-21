from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=255, unique=True)
    REQUIRED_FIELDS = ['username']

    phone_number = PhoneNumberField(unique=True,  verbose_name='Номер телефона')
    image_user = models.ImageField(upload_to='user_image/', default='user_image/default.png', verbose_name='Фото')
    
    def get_absolute_url(self):
        return f'/adminpanel/users/'
    
    def get_absolute_url(self):
        if self.is_staff == True:
            return f'/adminpanel/users/'
        else:
            return f'/accounts/profile/'
