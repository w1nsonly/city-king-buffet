from django.contrib import admin
from .models import MenuItem, OrderInfo

# Register your models here.

admin.site.register(MenuItem)  # Allow Menu Items in Django Admin
admin.site.register(OrderInfo)  # Allow Orders in Django Adminpython manage.py runserver



