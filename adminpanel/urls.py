from django.urls import path
from adminpanel.views import admin, products, users, orders, UpdateProduct, AddProduct, DelProduct



app_name = 'adminpanel'

urlpatterns = [
    path('', admin, name='admin'),
    path('products/', products, name='products'),
    path('users/', users, name='users'),
    path('orders/', orders, name='orders'),
    path('addproduct/', AddProduct.as_view(), name='add'),
    path('update/<str:pk>', UpdateProduct.as_view(), name='update'),
    path('del/<str:pk>', DelProduct.as_view(), name='del'),
]
