import os
import sys
import django


# Ensure the backend directory is in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from decimal import Decimal
from orders.models import MenuItem  # Import MenuItem model

# Dictionary of menu categories
menu_items = {
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
        {"name": "Weekend Dinner Buffet (Fri-Sun)", "price": 15.99},
    ],   
    "To Go": [
        {"name": "To Go", "price": 7.49},
        {"name": "Buffet To Go", "price": 10.99},
        {"name": "Drink", "price": 2.50},
    ],   
    "Appetizers": [
        {"name": "Spring Roll (2)", "price": 4.95},
        {"name": "Egg Roll", "price": 2.00},
        {"name": "Fried Biscuit (10)", "price": 5.95},
        {"name": "Fried Shrimp (11)", "price": 7.25},
        {"name": "Fried Dumpling (8)", "price": 7.95},
        {"name": "Steamed Dumpling (8)", "price": 7.95},
        {"name": "Crab Rangoon (8)", "price": 6.95},
        {"name": "Potato Skin (6)", "price": 6.95},
        {"name": "Fried Wonton (12)", "price": 5.95},
        {"name": "Chicken Teriyaki (5)", "price": 6.95},
        {"name": "Corn Nuggets (18)", "price": 6.95},
    ],
    "Soups": [
        {"name": "Wonton Soup", "price": 5.50},
        {"name": "Egg Drop Soup", "price": 5.50},
        {"name": "Chicken Noodle Soup", "price": 5.50},
        {"name": "Chicken Rice Soup", "price": 5.50},
        {"name": "Hot & Sour Soup", "price": 6.50},
        {"name": "Vegetable Soup", "price": 5.50},
        {"name": "House Special Soup", "price": 7.75},
        {"name": "Seafood Soup", "price": 7.75},
    ],
     "Sushi Rolls": [
        {"name": "California Roll (8)", "price": 7.99},
        {"name": "Pennsylvania Roll (8)", "price": 7.99},
        {"name": "Special Roll (8)", "price": 8.99},
        {"name": "Spicy Crabmeat Roll (8)", "price": 7.99},
        {"name": "Coconut Crabmeat Roll (8)", "price": 7.99},
    ],
    "Lunch Combos": [
        {"id_number": "L1", "name": "Chicken Chow Mein", "price": 8.25},
        {"id_number": "L2", "name": "Shrimp Chow Mein", "price": 8.25},
        {"id_number": "L3", "name": "Roast Pork Egg Foo Young", "price": 8.25},
        {"id_number": "L4", "name": "Roast Pork W. Chinese Veg", "price": 8.25},
        {"id_number": "L5", "name": "Chicken Lo Mein (Soft Noodles)", "price": 8.25},
        {"id_number": "L6", "name": "Pork Lo Mein (Soft Noodles)", "price": 8.25},
        {"id_number": "L7", "name": "Pepper Steak W. Onion", "price": 8.25},
        {"id_number": "L8", "name": "Moo Goo Gai Pan", "price": 8.25},
        {"id_number": "L9", "name": "Sweet & Sour Chicken", "price": 8.25},
        {"id_number": "L10", "name": "Shrimp W. Lobster Sauce", "price": 8.25},
        {"id_number": "L11", "name": "Shrimp W. Broccoli", "price": 8.25},
        {"id_number": "L12", "name": "Beef W. Broccoli", "price": 8.25},
        {"id_number": "L13", "name": "Chicken W. Broccoli", "price": 8.25},
        {"id_number": "L14", "name": "Sesame Chicken", "price": 8.25},
        {"id_number": "L15", "name": "Kung Po Chicken (Spicy)", "price": 8.25},
        {"id_number": "L16", "name": "Shrimp W. Garlic Sauce (Spicy)", "price": 8.25},
        {"id_number": "L17", "name": "Chicken W. Garlic Sauce (Spicy)", "price": 8.25},
        {"id_number": "L18", "name": "Szechuan Spice Shrimp (Spicy)", "price": 8.25},
        {"id_number": "L19", "name": "Sesame Beef", "price": 8.25},
        {"id_number": "L20", "name": "General Tso's Chicken (Spicy)", "price": 8.25},
        {"id_number": "L21", "name": "Chicken W. Cashew Nuts", "price": 8.25},
        {"id_number": "L22", "name": "Beef Hunan Style (Spicy)", "price": 8.25},
        {"id_number": "L23", "name": "Beef Szechuan Style (Spicy)", "price": 8.25},
        {"id_number": "L24", "name": "Chicken Hunan Style (Spicy)", "price": 8.25},
        {"id_number": "L25", "name": "Chicken Szechuan Style (Spicy)", "price": 8.25},
        {"id_number": "L26", "name": "Hot & Spicy Chicken", "price": 8.25},
        {"id_number": "L27", "name": "Hot & Spicy Shrimp", "price": 8.25},
        {"id_number": "L28", "name": "Honey Chicken", "price": 8.25},
        {"id_number": "L29", "name": "Chicken Teriyaki", "price": 8.25},
        {"id_number": "L30", "name": "Black Pepper Chicken", "price": 8.25},
        {"id_number": "L31", "name": "Bourbon Chicken", "price": 8.25},
    ],
    "Special Combos": [
        {"id_number": "C1", "name": "Chicken Chow Mein", "price": 10.25},
        {"id_number": "C2", "name": "Shrimp Chow Mein", "price": 10.25},
        {"id_number": "C3", "name": "Roast Pork Egg Foo Young", "price": 10.25},
        {"id_number": "C4", "name": "Roast Pork W. Chinese Veg", "price": 10.25},
        {"id_number": "C5", "name": "Chicken Lo Mein (Soft Noodles)", "price": 10.25},
        {"id_number": "C6", "name": "Pork Lo Mein (Soft Noodles)", "price": 10.25},
        {"id_number": "C7", "name": "Pepper Steak W. Onion", "price": 10.25},
        {"id_number": "C8", "name": "Moo Goo Gai Pan", "price": 10.25},
        {"id_number": "C9", "name": "Sweet & Sour Chicken", "price": 10.25},
        {"id_number": "C10", "name": "Shrimp W. Lobster Sauce", "price": 10.25},
        {"id_number": "C11", "name": "Shrimp W. Broccoli", "price": 10.25},
        {"id_number": "C12", "name": "Beef W. Broccoli", "price": 10.25},
        {"id_number": "C13", "name": "Chicken W. Broccoli", "price": 10.25},
        {"id_number": "C14", "name": "Sesame Chicken", "price": 10.25},
        {"id_number": "C15", "name": "Kung Po Chicken (Spicy)", "price": 10.25},
        {"id_number": "C16", "name": "Shrimp W. Garlic Sauce (Spicy)", "price": 10.25},
        {"id_number": "C17", "name": "Chicken W. Garlic Sauce (Spicy)", "price": 10.25},
        {"id_number": "C18", "name": "Szechuan Spice Shrimp (Spicy)", "price": 10.25},
        {"id_number": "C19", "name": "Sesame Beef", "price": 10.25},
        {"id_number": "C20", "name": "General Tso's Chicken (Spicy)", "price": 10.25},
        {"id_number": "C21", "name": "Chicken W. Cashew Nuts", "price": 10.25},
        {"id_number": "C22", "name": "Beef Hunan Style (Spicy)", "price": 10.25},
        {"id_number": "C23", "name": "Beef Szechuan Style (Spicy)", "price": 10.25},
        {"id_number": "C24", "name": "Chicken Hunan Style (Spicy)", "price": 10.25},
        {"id_number": "C25", "name": "Chicken Szechuan Style (Spicy)", "price": 10.25},
        {"id_number": "C26", "name": "Hot & Spicy Chicken", "price": 10.25},
        {"id_number": "C27", "name": "Hot & Spicy Shrimp", "price": 10.25},
        {"id_number": "C28", "name": "Honey Chicken", "price": 10.25},
        {"id_number": "C29", "name": "Chicken Teriyaki", "price": 10.25},
        {"id_number": "C30", "name": "Black Pepper Chicken", "price": 10.25},
        {"id_number": "C31", "name": "Bourbon Chicken", "price": 10.25},
    ],
    "Chow Mein": [
        {"id_number": 17, "name": "Chicken Chow Mein", "price": 8.95},
        {"id_number": 18, "name": "Roast Pork Chow Mein", "price": 8.95},
        {"id_number": 19, "name": "Beef Chow Mein", "price": 8.95},
        {"id_number": 20, "name": "Shrimp Chow Mein", "price": 8.95},
        {"id_number": 21, "name": "Vegetable Chow Mein", "price": 8.95},
        {"id_number": 22, "name": "House Special Chow Mein", "price": 8.95},
    ],
    "Chop Suey": [
        {"id_number": 23, "name": "Chicken Chop Suey", "price": 8.95},
        {"id_number": 24, "name": "Roast Pork Chop Suey", "price": 8.95},
        {"id_number": 25, "name": "Beef Chop Suey", "price": 8.95},
        {"id_number": 26, "name": "Shrimp Chop Suey", "price": 8.95},
        {"id_number": 27, "name": "Vegetable Chop Suey", "price": 8.95},
        {"id_number": 28, "name": "House Special Chop Suey", "price": 8.95},
    ],
    "Lo Mein": [
        {"id_number": 29, "name": "Plain Lo Mein", "price": 8.95},
        {"id_number": 30, "name": "Vegetable Lo Mein", "price": 8.95},
        {"id_number": 31, "name": "Chicken Lo Mein", "price": 8.95},
        {"id_number": 32, "name": "Roast Pork Lo Mein", "price": 8.95},
        {"id_number": 33, "name": "Beef Lo Mein", "price": 8.95},
        {"id_number": 34, "name": "Shrimp Lo Mein", "price": 8.95},
        {"id_number": 35, "name": "House Special Lo Mein", "price": 9.95},
    ],
    "Mei Fun": [
        {"id_number": 36, "name": "Roast Pork Mei Fun", "price": 8.75},
        {"id_number": 37, "name": "Chicken Mei Fun", "price": 8.75},
        {"id_number": 38, "name": "Shrimp Mei Fun", "price": 8.75},
        {"id_number": 39, "name": "Beef Mei Fun", "price": 8.75},
        {"id_number": 40, "name": "Vegetable Mei Fun", "price": 8.75},
        {"id_number": 41, "name": "House Special Mei Fun", "price": 10.25},
        {"id_number": 42, "name": "Singapore Mei Fun (Spicy)", "price": 10.25},
    ],
    "Fried Rice": [
        {"id_number": 43, "name": "Plain Fried Rice", "price": 8.95},
        {"id_number": 44, "name": "Vegetable Fried Rice", "price": 8.95},
        {"id_number": 45, "name": "Chicken Fried Rice", "price": 9.75},
        {"id_number": 46, "name": "Roast Pork Fried Rice", "price": 9.75},
        {"id_number": 47, "name": "Beef Fried Rice", "price": 9.75},
        {"id_number": 48, "name": "Shrimp Fried Rice", "price": 9.75},
        {"id_number": 49, "name": "House Special Fried Rice", "price": 10.25},
    ],
    "Egg Foo Young": [
        {"id_number": 50, "name": "Mushroom Egg Foo Young", "price": 9.75},
        {"id_number": 51, "name": "Chicken Egg Foo Young", "price": 9.75},
        {"id_number": 52, "name": "Roast Pork Egg Foo Young", "price": 9.75},
        {"id_number": 53, "name": "Beef Egg Foo Young", "price": 9.75},
        {"id_number": 54, "name": "Shrimp Egg Foo Young", "price": 9.75},
    ],
    "Vegetable": [
        {"id_number": 55, "name": "Sauteed Broccoli", "price": 8.99},
        {"id_number": 56, "name": "Sauteed Chinese Vegetable", "price": 8.99},
        {"id_number": 57, "name": "Mixed Vegetable", "price": 8.99},
        {"id_number": 58, "name": "String Beans", "price": 8.99},
        {"id_number": 59, "name": "Broccoli in Garlic Sauce (Spicy)", "price": 8.99},
        {"id_number": 60, "name": "Mixed Vegetable in Garlic Sauce (Spicy)", "price": 8.99},
        {"id_number": 61, "name": "Butter Potato", "price": 8.99},
    ],
    "Shrimp": [
        {"id_number": 62, "name": "Shrimp W. Lobster Sauce", "price": 10.50},
        {"id_number": 63, "name": "Shrimp W. Vegetable", "price": 10.50},
        {"id_number": 64, "name": "Shrimp W. Broccoli", "price": 10.50},
        {"id_number": 65, "name": "Shrimp W. Curry Sauce", "price": 10.50},
        {"id_number": 66, "name": "Hot & Spicy Shrimp", "price": 10.50},
        {"id_number": 67, "name": "Shrimp W. Garlic Sauce (Spicy)", "price": 10.50},
        {"id_number": 68, "name": "Shrimp W. Cashew Nuts", "price": 10.50},
        {"id_number": 69, "name": "Kung Po Shrimp (Spicy)", "price": 10.50},
        {"id_number": 70, "name": "Shrimp W. Mixed Vegetable", "price": 10.50},
        {"id_number": 71, "name": "Coconut Shrimp", "price": 11.50},
        {"id_number": 72, "name": "Black Pepper Shrimp", "price": 14.99},
    ], 
    "Beef": [
        {"id_number": 73, "name": "Kung Po Beef W. Peanut (Spicy)", "price": 10.25},
        {"id_number": 74, "name": "Beef W. Garlic Sauce (Spicy)", "price": 10.25},
        {"id_number": 75, "name": "Beef W. Mixed Vegetables", "price": 10.25},
        {"id_number": 76, "name": "Beef Szechuan Style (Spicy)", "price": 10.25},
        {"id_number": 77, "name": "Beef Hunan Style (Spicy)", "price": 10.25},
        {"id_number": 78, "name": "Beef W. Mushroom & Pea Pod", "price": 10.25},
    ],
    "Pork": [
        {"id_number": 79, "name": "Roast Pork W. Broccoli", "price": 9.95},
        {"id_number": 80, "name": "Roast Pork W. Chinese Veg", "price": 9.95},
        {"id_number": 81, "name": "Kung Po Pork (Spicy)", "price": 9.95},
        {"id_number": 82, "name": "Pork Hunan Style (Spicy)", "price": 9.95},
        {"id_number": 83, "name": "Pork In Garlic Sauce (Spicy)", "price": 9.95},
        {"id_number": 84, "name": "Roast Pork W. Cashew Nuts", "price": 9.95},
    ],
    "Chicken": [
        {"id_number": 85, "name": "Chicken W. Broccoli", "price": 10.25},
        {"id_number": 86, "name": "Chicken W. String Beans", "price": 10.25},
        {"id_number": 87, "name": "Spicy Curry Chicken", "price": 10.25},
        {"id_number": 88, "name": "Chicken W. Cashew Nuts", "price": 10.25},
        {"id_number": 89, "name": "Chicken In Garlic Sauce (Spicy)", "price": 10.25},
        {"id_number": 90, "name": "Chicken Teriyaki", "price": 10.25},
        {"id_number": 91, "name": "Sweet & Sour Chicken", "price": 10.25},
        {"id_number": 92, "name": "Kung Po Chicken (Spicy)", "price": 10.25},
        {"id_number": 93, "name": "Moo Gao Gai Pan (Chicken)", "price": 10.25},
        {"id_number": 94, "name": "Chicken W. Mixed Vegetable", "price": 10.25},
        {"id_number": 95, "name": "Chicken W. Broccoli In Garlic Sauce", "price": 10.25},
        {"id_number": 96, "name": "Chicken Hunan Style (Spicy)", "price": 10.25},
        {"id_number": 97, "name": "Chicken Szechuan Style (Spicy)", "price": 10.25},
        {"id_number": 98, "name": "Hot & Spicy Chicken", "price": 10.25},
        {"id_number": 99, "name": "Black Pepper Chicken", "price": 10.25},
        {"id_number": 100, "name": "Bourbon Chicken", "price": 10.25},
    ],
    "Chef Specials": [
        {"id_number": "S1", "name": "Happy Family", "price": 13.95},
        {"id_number": "S2", "name": "Seafood Combination", "price": 14.75},
        {"id_number": "S3", "name": "Mandarin Triple Crown", "price": 12.25},
        {"id_number": "S4", "name": "Double Treat", "price": 12.25},
        {"id_number": "S5", "name": "General Tso's Shrimp (Spicy)", "price": 11.95},
        {"id_number": "S6", "name": "Sesame Beef", "price": 12.50},
        {"id_number": "S7", "name": "Sesame Chicken", "price": 10.99},
        {"id_number": "S8", "name": "Hunan Shrimp (Spicy)", "price": 11.50},
        {"id_number": "S9", "name": "Dragon & Phoenix", "price": 11.75},
        {"id_number": "S10", "name": "General Tso's Chicken (Spicy)", "price": 11.50},
        {"id_number": "S11", "name": "Orange Chicken (Spicy)", "price": 11.59},
        {"id_number": "S12", "name": "Orange Beef (Spicy)", "price": 11.99},
        {"id_number": "S13", "name": "Triple Delight W. Garlic Sauce (Spicy)", "price": 10.75},
        {"id_number": "S14", "name": "Kung Po Triple Delight (Spicy)", "price": 11.75},
        {"id_number": "S15", "name": "Hunan Triple (Spicy)", "price": 11.75},
        {"id_number": "S16", "name": "Shrimp W. Szechuan Sauce (Spicy)", "price": 11.75},
        {"id_number": "S17", "name": "Mongolian Beef", "price": 11.75},
        {"id_number": "S18", "name": "Honey Chicken", "price": 11.75},
    ],
    "Diet Menu": [
        {"id_number": "D1", "name": "Bean Curd & Mixed Vegetables", "price": 8.50},
        {"id_number": "D2", "name": "Mixed Vegetables", "price": 8.50},
        {"id_number": "D3", "name": "Steamed Shrimp W. Broccoli", "price": 10.50},
        {"id_number": "D4", "name": "Chicken W. Broccoli", "price": 9.95},
        {"id_number": "D5", "name": "Chicken W. Vegetables", "price": 9.95},
        {"id_number": "D6", "name": "Steamed Broccoli", "price": 8.50},
        {"id_number": "D7", "name": "Shrimp W. Chinese Vegetables", "price": 10.50},
    ],
    "Side Orders": [
        {"name": "Delivery Fee", "price": 1.00},
        {"name": "White Rice", "price": 3.50},
        {"name": "Fortune Cookies (10)", "price": 5.00},
        {"name": "Fried Noodles (Big Bag)", "price": 3.00},
        {"name": "Sauce", "price": 1.50},
    ],
}


# script to update if added or updated
for category, items in menu_items.items():
    for item in items:
        obj, created = MenuItem.objects.get_or_create(
            name=item["name"], category=category, id_number=item.get("id_number"),
            defaults={"category": category, "price": item["price"], "id_number": item.get("id_number")}  # Set defaults
        )

        if created:
            print(f"✅ Added: {item['name']} (Category: {category}) - ID: {item.get('id_number')}")
        else:
            updated = False  # Track if any update is needed
            
            updates = []  # Store update messages to print only if something changes

            # Check and update category
            if str(obj.category) != str(category):
                updates.append(f"Category: {obj.category} → {category}")
                obj.category = category
                updated = True

            # Check and update name    
            if (obj.name) != (item["name"]):
                print(type(obj.name), obj.name)
                print(type(item["name"]), item["name"])
                updates.append(f"Name: {obj.name} → {item['name']}")
                obj.name = item['name']
                updated = True

            # Check and update price
            if Decimal(obj.price) != Decimal(str(item["price"])): 
                updates.append(f"Price: ${obj.price} → ${item['price']}")
                obj.price = item["price"]
                updated = True

            # Check and update id_number
            if str(obj.id_number) != str(item.get("id_number")):
                updates.append(f"ID Number: {obj.id_number} → {item.get('id_number')}")
                obj.id_number = item.get("id_number")
                updated = True

            # Save only if updates were made
            if updated:
                obj.save()
                print(f"🔄 Updated {item['name']} (Category: {category}) - " + ", ".join(updates))

