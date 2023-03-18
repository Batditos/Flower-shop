from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=255, unique=True)
    REQUIRED_FIELDS = ['username']

    phone_number = PhoneNumberField(unique=True)
    image_user = models.ImageField(
        upload_to='user_image/', default='user_image/default.png')
