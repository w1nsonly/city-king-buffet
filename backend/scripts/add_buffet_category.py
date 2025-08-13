# restaurant/scripts/add_buffet_category.py

import os
import sys
from decimal import Decimal
import django

# Ensure manage.py’s parent dir is on sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()
# --------------------------------------------------------------

from restaurant.models import BuffetCategory

from restaurant.models import BuffetCategory

# Professional subtitles
LUNCH_SUBTITLE   = "Mon-Sat • Open-4 PM"
DINNER_SUBTITLE  = "Mon-Thu • 4 PM-Close"
WEEKEND_SUBTITLE = "Fri-Sat • 4 PM-Close; Sun All Day • Kids pay dinner."
TOGO_SUBTITLE    = "Priced by weight (per pound)."

CATEGORIES = {
    "Lunch Buffet":   LUNCH_SUBTITLE,
    "Dinner Buffet":  DINNER_SUBTITLE,
    "Weekend Buffet": WEEKEND_SUBTITLE,
    "To Go":          TOGO_SUBTITLE,
}

def main():
    for name, subtitle in CATEGORIES.items():
        obj, created = BuffetCategory.objects.update_or_create(name=name, defaults={"subtitle": subtitle},)
        print(("Created" if created else "Updated") + f": {obj.name} — subtitle: '{obj.subtitle}'")

if __name__ == "__main__":
    main()