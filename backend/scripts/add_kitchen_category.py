# restaurant/scripts/add_kitchen_category.py

import os
import sys
import django

# Ensure manage.py’s parent dir is on sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
# --------------------------------------------------------------

from restaurant.models import KitchenCategory

COMBO_SUBTITLE = "Served with fried rice and an egg roll"
WHITE_RICE_SUBTITLE = "Served with steamed white rice"

categories = {
    "Appetizers": "",
    "Soups": "",
    "Chow Mein": WHITE_RICE_SUBTITLE,
    "Chop Suey": WHITE_RICE_SUBTITLE,
    "Lo Mein": "",
    "Mei Fun": "",
    "Fried Rice": "",
    "Egg Foo Young": WHITE_RICE_SUBTITLE,
    "Vegetable": WHITE_RICE_SUBTITLE,
    "Shrimp": WHITE_RICE_SUBTITLE,
    "Beef": WHITE_RICE_SUBTITLE,
    "Pork": WHITE_RICE_SUBTITLE,
    "Chicken": WHITE_RICE_SUBTITLE,
    "Lunch Combos": COMBO_SUBTITLE,
    "Special Combos": COMBO_SUBTITLE,
    "Chef Specials": WHITE_RICE_SUBTITLE,
    "Diet Menu": WHITE_RICE_SUBTITLE,
    "Sushi Rolls": "",
    "Side Orders": "",
}

def main():
    for name, subtitle in categories.items():
        obj, created = KitchenCategory.objects.update_or_create(name=name,defaults={"subtitle": subtitle},)

        print(("Created" if created else "Updated") + f": {obj.name} — subtitle: '{obj.subtitle}'")

if __name__ == "__main__":
    main()
