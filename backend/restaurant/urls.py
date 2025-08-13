# restaurant/urls.py

from django.urls import path
from .views import BuffetCategoryList, BuffetItemList, KitchenCategoryList, KitchenItemList
from restaurant.views import chat

urlpatterns = [
    # Category endpoints
    path('category/buffet', BuffetCategoryList.as_view(), name='kitchen-categories'),
    path('category/kitchen', KitchenCategoryList.as_view(), name='kitchen-categories'),

    # Menu endpoints
    path('menu/buffet/', BuffetItemList.as_view(), name='buffet-items'),
    path('menu/kitchen/', KitchenItemList.as_view(), name='kitchen-items'),

    
    # Chat endpoint
    path('chat/', chat, name='restaurant-chat'),

]