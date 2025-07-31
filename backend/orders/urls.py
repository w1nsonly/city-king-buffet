from django.urls import path
from .views import BuffetItemList, MenuItemList, OrderCreate

urlpatterns = [
    path('buffet/', BuffetItemList.as_view(), name='buffet-list'),
    path('menu/', MenuItemList.as_view(), name='menu-list'),
    path('order/', OrderCreate.as_view(), name='order-create'),
    
]