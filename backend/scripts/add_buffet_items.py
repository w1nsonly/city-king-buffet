# restaurant/scripts/add_buffet_items.py

import os
import sys
from decimal import Decimal
import django

# Ensure manage.py’s parent dir is on sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
# --------------------------------------------------------------

from restaurant.models import BuffetItem, BuffetCategory

buffet_items = {
        "Lunch Buffet": [
            {"name": "Lunch Buffet", "price": 11.99},
            {"name": "L. Kid 3-5 Year Old", "price": 6.99},
            {"name": "L. Kid 6-10 Year Old", "price": 7.99},
        ],
        "Dinner Buffet": [
            {"name": "Dinner Buffet", "price": 14.99},
            {"name": "D. Kid 3-5 Year Old", "price": 7.99},
            {"name": "D. Kid 6-10 Year Old", "price": 9.99},
        ],   
        "Weekend Buffet": [
            {"name": "Weekend Dinner Buffet", "price": 15.99},
        ],   
        "To Go": [
            {"name": "To Go", "price": 7.49},
            {"name": "Hibachi/Sushi To Go", "price": 10.99},
        ],   
}

def main():
   for category_name, items in buffet_items.items():
        # categories were created by category script; fall back to get_or_create
        category, _ = BuffetCategory.objects.get_or_create(name=category_name)

        for item in items:
            name = item["name"]
            price = Decimal(str(item["price"]))

            obj, created = BuffetItem.objects.update_or_create(category=category, name=name, defaults={"price": price})
            action = "Created" if created else "Updated"
            print(f"{action}: {category.name} → {obj.name} (${price})")

if __name__ == "__main__":
    main()