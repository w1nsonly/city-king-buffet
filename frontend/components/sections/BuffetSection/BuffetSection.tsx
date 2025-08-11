// components/sections/BuffetSection/BuffetSection.tsx

'use client'
import React, { useEffect, useState } from "react";
import axios from "axios";
import BuffetCategory from "@/components/menu/BuffetCategory";
import { BuffetItem } from "@/types";
import ItemModal from "@/components/modal/ItemModal";
import { Playfair_Display } from "next/font/google";

const playfair = Playfair_Display({
  subsets: ["latin"],
});

export default function BuffetSection() {
    const API_BASE = process.env.NEXT_PUBLIC_API_BASE!;
    const [menuItems, setMenuItems] = useState<BuffetItem[]>([]);
    const [modal, setModal] = useState(false);
    const [selectedItem, setSelectedItem] = useState<BuffetItem| null>(null);

    
    function toggleModal(item?: BuffetItem) {
        if (modal) {
            setSelectedItem(null);
        } else if (item) {
            setSelectedItem(item);
        }
        setModal(!modal)
    }

    useEffect(() => {
        axios
        .get<BuffetItem[]>(`${API_BASE}restaurant/menu/buffet`)
        .then((res) => setMenuItems(res.data))
        .catch((err) => console.error("Error fetching menu:", err));
    }, []);

  return (
    
    <section id="buffet" className="w-full overflow-x-hidden bg-[url('/lightbeige.jpg')] py-10">
        <div className="w-full max-w-[1000px] mx-auto px-4 sm:px-6">
            <div className="p-5 bg-[#fffdf5] shadow-[0_4px_8px_rgba(0,0,0,0.1)] rounded-[10px]">
                <h2 className={`${playfair.className} text-center text-4xl font-bold mb-6 text-black [-webkit-text-fill-color:#000]`}>Buffet Menu</h2>

                {/* mobile-first grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 w-full">
                {/* Left column */}
                    <div className="flex flex-col gap-5 min-w-0">
                        {["Lunch Buffet", "To Go (Priced Per Pound)"].map((category) => (
                            <BuffetCategory 
                            key={category} 
                            category={category} 
                            items={menuItems.filter((i) => i.category === category)}
                            onClick={toggleModal}
                            />
                        ))}
                    </div>

                    {/* Right column */}
                    <div className="flex flex-col gap-5 min-w-0">
                        {["Dinner Buffet", "Weekend Buffet"].map((category) => (
                            <BuffetCategory 
                            key={category} 
                            category={category} 
                            items={menuItems.filter((i) => i.category === category)}
                            onClick={toggleModal}
                            />
                        ))}
                    </div>
                </div>

                {selectedItem && (
                    <ItemModal modal={modal} toggleModal={toggleModal} item={selectedItem} price={Number(selectedItem.price)}/>
                )}

                {/* View Kitchen Button */}
                <div className="mt-6 flex gap-3 justify-center sm:justify-start">
                    <a href="/kitchen" className="px-5 py-2 rounded-md border border-[#7f1d1d] text-[#7f1d1d] hover:bg-[#7f1d1d] hover:text-white transition">
                        View Kitchen Menu
                    </a>
                </div>
            </div>
        </div>
    </section>
    );
}
