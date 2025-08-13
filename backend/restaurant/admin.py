# restaurant/admin.py

from django.contrib import admin
from .models import BuffetCategory, BuffetItem, KitchenCategory, KitchenItem

# Register your models here.
admin.site.register(BuffetCategory)
admin.site.register(BuffetItem)
admin.site.register(KitchenCategory)
admin.site.register(KitchenItem)




