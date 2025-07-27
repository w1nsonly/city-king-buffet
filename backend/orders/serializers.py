from rest_framework import serializers
from .models import MenuItem, OrderInfo

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  # Includes all fields (name, price)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = '__all__'  # Includes all fields (customer info, items, price)
