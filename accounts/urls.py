from django.urls import path
from accounts.views import UpdateProfile, profile_views, user_login, logout_views, register, OrderViews

app_name = "accounts"

urlpatterns = [
    path('profile/', profile_views, name='profile_views'),
    path('login/', user_login, name='user_login'),
    path('logout/', logout_views, name='logout_views'),
    path('register/', register, name='register'),
    path('update/<str:pk>', UpdateProfile.as_view(), name='updateprofile'),
    path('order/<str:pk>', OrderViews.as_view() , name='views')
]
