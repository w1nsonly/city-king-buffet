# restaurant/serializers.py

from rest_framework import serializers
from .models import BuffetItem, MenuItem

class BuffetItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuffetItem
        fields = '__all__'  # Includes all fields (name, price, category)
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  # Includes all fields (id_number, name, price, category)