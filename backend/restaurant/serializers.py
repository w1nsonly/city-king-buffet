# restaurant/serializers.py

from rest_framework import serializers
from .models import BuffetCategory, BuffetItem, KitchenCategory, KitchenItem

class BuffetCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BuffetCategory
        fields = '__all__'  # Includes all fields (name, subtitle)

class BuffetItemSerializer(serializers.ModelSerializer):
    # Return the category NAME for reads, so your frontend stays the same
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = BuffetItem
        fields = '__all__'  # Includes all fields (name, price, category)

class KitchenCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = KitchenCategory
        fields = '__all__'  # Includes all fields (name, subtitle)
        
class KitchenItemSerializer(serializers.ModelSerializer):
    # Return the category NAME for reads, so your frontend stays the same
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = KitchenItem
        fields = '__all__'  # Includes all fields (category, id_number, name, price, is_spicy)