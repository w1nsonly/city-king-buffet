from django.shortcuts import render
from rest_framework import generics
from .models import BuffetItem, MenuItem, OrderInfo
from .serializers import BuffetItemSerializer, MenuItemSerializer, OrderSerializer
from django.http import JsonResponse

# Create your views here.


# GET all menu items
class BuffetItemList(generics.ListAPIView):
    queryset = BuffetItem.objects.all()
    serializer_class = BuffetItemSerializer

class MenuItemList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# POST an order
class OrderCreate(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSerializer


