# restaurant/models.py

from django.db import models

# Create your models here.
class BuffetCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class BuffetItem(models.Model):
    category = models.ForeignKey('BuffetCategory', on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"


class KitchenCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class KitchenItem(models.Model):
    category = models.ForeignKey('KitchenCategory', on_delete=models.CASCADE, related_name='items')
    id_number = models.CharField(max_length=10, unique=False, blank=True, null=True)  # Example: "C15"
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_spicy = models.BooleanField(default=False)

    class Meta:
        ordering = ["category", "id"]

    def __str__(self):
        return f"{self.id_number} - {self.name}"


    
    