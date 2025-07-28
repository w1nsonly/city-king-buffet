from django.contrib import admin
from .models import BuffetItem, MenuItem, OrderInfo

# Register your models here.
admin.site.register(BuffetItem)
admin.site.register(MenuItem)  # Allow Menu Items in Django Admin
admin.site.register(OrderInfo)  # Allow Orders in Django Adminpython manage.py runserver



