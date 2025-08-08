'use client'
import React, { useState, useEffect } from "react";
import axios from "axios";
import MenuCategory from "@/menu/MenuCategory";
import { MenuItem } from "@/types";

export default function MenuSection() {
  
  const [menuItems, setMenuItems] = useState<MenuItem[]>([]);

  useEffect(() => {
    axios
      .get<MenuItem[]>("http://127.0.0.1:8000/restaurant/menu/regular")
      .then((res) => setMenuItems(res.data))
      .catch((err) => console.error("Error fetching menu:", err));
  }, []);

  return (
    <div
      className="
        max-w-[1000px] mx-auto my-5 
        p-5 bg-[#fffdf5] 
        shadow-[0_4px_8px_rgba(0,0,0,0.1)] 
        rounded-[10px]
      "
    >
      <h2 className="text-3xl font-bold mb-6">Kitchen Menu</h2>

      <div className="grid grid-cols-2 gap-5">
        {/* Left column */}
        <div className="flex flex-col gap-5">
          {[
            "Appetizers",
            "Soups",
            "Chow Mein",
            "Chop Suey",
            "Lo Mein",
            "Mei Fun",
            "Fried Rice",
            "Egg Foo Young",
            "Vegetable",
            "Shrimp",
            "Beef",
            "Pork",
            "Chicken",
          ].map((category) => (
            <MenuCategory
              key={category}
              category={category}
              items={menuItems.filter((i) => i.category === category)}
            />
          ))}
        </div>

        {/* Right column */}
        <div className="flex flex-col gap-5">
          {[
            "Lunch Combos",
            "Special Combos",
            "Chef Specials",
            "Diet Menu",
            "Sushi Rolls",
            "Side Orders",
          ].map((category) => (
            <MenuCategory
              key={category}
              category={category}
              items={menuItems.filter((i) => i.category === category)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
