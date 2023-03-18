from django.urls import path
from accounts.views import profile_views, user_login, logout_views, register

app_name = "accounts"

urlpatterns = [
    path('profile/', profile_views, name='profile_views'),
    path('login/', user_login, name='user_login'),
    path('logout/', logout_views, name='logout_views'),
    path('register/', register, name='register'),
]
