# restaurant/admin.py
from django.contrib import admin
from .models import BuffetItem, MenuItem

# Register your models here.
admin.site.register(BuffetItem)
admin.site.register(MenuItem)  # Allow Menu Items in Django Admin




