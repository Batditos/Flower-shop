from .models import User
from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'phone_number']
    list_editable = [ 'first_name', 'phone_number']


admin.site.register(User, ProfileAdmin)
