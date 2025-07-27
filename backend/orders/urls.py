from django.urls import path
from .views import MenuItemList, OrderCreate

urlpatterns = [
    path('menu/', MenuItemList.as_view(), name='menu-list'),
    path('order/', OrderCreate.as_view(), name='order-create')
]