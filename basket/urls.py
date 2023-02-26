from django.urls import path
from . import views


app_name = 'basket'

urlpatterns = [
    path('', views.basket_detail, name='basket_detail'),
    path('add/<str:product_id>/', views.basket_add, name='basket_add'),
    path('remove/<str:product_id>/', views.basket_remove, name='basket_remove'),
    path('minus/<str:product_id>/', views.minus_quantity, name='minus_quantity'),
    path('plus/<str:product_id>/', views.plus_quantity, name='plus_quantity'),
]
