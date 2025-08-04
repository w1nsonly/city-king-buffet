'use client'
import React, { useEffect, useState } from "react"
import axios from "axios";
import BuffetCategory from "@/menu/BuffetCategory";
import { BuffetItem } from "@/types";


export default function BuffetItems() {

    const [menuItems, setMenuItems] = useState<BuffetItem[]>([]);

    useEffect(() => {
        axios
        .get<BuffetItem[]>("http://127.0.0.1:8000/restaurant/menu/buffet")
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
            <h2 className="text-3xl font-bold mb-6">Buffet Menu</h2>
        
            <div className="grid grid-cols-2 gap-5">
                {/* Left column */}
                <div className="flex flex-col gap-5">
                    {[
                    "Lunch Buffet",
                    "To Go",
                    
                    ].map((category) => (
                    <BuffetCategory
                        key={category}
                        category={category}
                        items={menuItems.filter((i) => i.category === category)}
                    />
                    ))}
                </div>
        
                {/* Right column */}
                <div className="flex flex-col gap-5">
                    {[
                    "Dinner Buffet",
                    "Weekend Buffet",
                    
                    ].map((category) => (
                    <BuffetCategory
                        key={category}
                        category={category}
                        items={menuItems.filter((i) => i.category === category)}
                    />
                    ))}
                </div>
            </div>
        </div>
    )
}