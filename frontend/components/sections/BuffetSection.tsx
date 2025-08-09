// components/sections/BuffetSection.tsx

'use client'
import React, { useEffect, useState } from "react"
import axios from "axios";
import BuffetCategory from "@/components/menu/BuffetCategory";
import { BuffetItem } from "@/types";


export default function BuffetSection() {

    const [menuItems, setMenuItems] = useState<BuffetItem[]>([]);
    
    const API_BASE = process.env.NEXT_PUBLIC_API_BASE!;

    useEffect(() => {
        axios
        .get<BuffetItem[]>(`${API_BASE}restaurant/menu/buffet`)
        .then((res) => setMenuItems(res.data))
        .catch((err) => console.error("Error fetching menu:", err));
    }, []);

    return (
        <div className="bg-[url('/lightbeige.jpg')] py-10">
            <div className="max-w-[1000px] mx-auto p-5 bg-[#fffdf5] shadow-[0_4px_8px_rgba(0,0,0,0.1)] rounded-[10px]">
                <h2 className="text-center text-3xl font-bold mb-6">Buffet Menu</h2>
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

                <div className="mt-6 flex gap-3">
                    <a href="/kitchen" className="px-5 py-2 rounded-md border border-[#7f1d1d] text-[#7f1d1d] hover:bg-[#7f1d1d] hover:text-white transition">
                        View Kitchen Menu
                    </a>
                </div>
            </div>
        </div>
    )
}