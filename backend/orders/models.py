from django.db import models

# Create your models here.


class MenuItem(models.Model):
    id_number = models.CharField(max_length=10, unique=True, blank=True, null=True)  # Example: "C15"
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_number} - {self.name}"

    

class OrderInfo(models.Model):
    customer_name = models.CharField(max_length=100)  # Store customer's name
    customer_phone = models.CharField(max_length=15)  # Store phone number
    customer_email = models.EmailField()  # Store email
    items = models.ManyToManyField(MenuItem)  # Order can have multiple menu items
    special_instructions = models.TextField(blank=True, null=True)  # Optional special instructions
    total_price = models.DecimalField(max_digits=6, decimal_places=2)  # Store total price
    created_at = models.DateTimeField(auto_now_add=True)  # Store order creation time

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"
