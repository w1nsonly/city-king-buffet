# restaurant/urls.py

from django.urls import path
from .views import BuffetItemList, MenuItemList
from restaurant.views import chat

urlpatterns = [
    # Menu endpoints
    path('menu/buffet/', BuffetItemList.as_view(), name='buffet-items'),
    path('menu/regular/', MenuItemList.as_view(), name='menu-items'),
    
    # Chat endpoint
    path('chat/', chat, name='restaurant-chat'),

]