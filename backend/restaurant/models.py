# restaurant/models.py

from django.db import models

# Create your models here.

class BuffetItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"


class MenuItem(models.Model):
    id_number = models.CharField(max_length=10, unique=False, blank=True, null=True)  # Example: "C15"
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_number} - {self.name}"

    