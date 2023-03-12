from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('profile/', views.profile_views, name='profile_views'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_views, name='logout_views'),
    path('register/', views.register, name='register'),
]
