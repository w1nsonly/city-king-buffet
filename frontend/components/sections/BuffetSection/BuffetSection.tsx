// components/sections/BuffetSection/BuffetSection.tsx

'use client'
import React, { useEffect, useState } from "react";
import axios from "axios";
import BuffetCategory from "@/components/menu/BuffetCategory";
import { BuffetCategoryTypes, BuffetItemTypes } from "@/types";
import ItemModal from "@/components/modal/ItemModal";
import { Playfair_Display } from "next/font/google";

const playfair = Playfair_Display({
    subsets: ["latin"],
});

export default function BuffetSection() {
    const API_BASE = process.env.NEXT_PUBLIC_API_BASE!;
    const [buffetItems, setBuffetItems] = useState<BuffetItemTypes[]>([]);
    const [categoriesMeta, setCategoriesMeta] = useState<BuffetCategoryTypes[]>([]);
    const [modal, setModal] = useState(false);
    const [selectedItem, setSelectedItem] = useState<BuffetItemTypes| null>(null);

    
    function toggleModal(item?: BuffetItemTypes) {
        if (modal) {
            setSelectedItem(null);
        } else if (item) {
            setSelectedItem(item);
        }
        setModal(!modal)
    }

    useEffect(() => {
        (async () => {
            try {
                const [itemsRes, catsRes] = await Promise.all([
                    axios.get<BuffetItemTypes[]>(`${API_BASE}restaurant/menu/buffet`),
                    axios.get<BuffetCategoryTypes[]>(`${API_BASE}restaurant/category/buffet`),
                ]);
                setBuffetItems(itemsRes.data);
                setCategoriesMeta(catsRes.data);
            } catch (err) {
                console.error("Error fetching kitchen data:", err);
            }
        })();
    }, [API_BASE]);

    const subtitleFor = (name: string) =>
        categoriesMeta.find(c => c.name === name)?.subtitle || "";

    const buffetCategories = ["Lunch Buffet", "Dinner Buffet", "Weekend Buffet", "To Go"];

    // Merge both into one map of order classes
    const orderMap: Record<string, string> = {
        "Lunch Buffet":   "order-1 sm:order-1",
        "Dinner Buffet":  "order-2 sm:order-3",
        "Weekend Buffet": "order-3 sm:order-2",
        "To Go":          "order-4 sm:order-4",
    };
    return (
    
    <section id="buffet" className="w-full overflow-x-hidden bg-[url('/light-beige.jpg')] py-10">
        <div className="w-full max-w-[1000px] mx-auto px-4 sm:px-6">
            <div className="p-5 bg-[#fffdf5] shadow-[0_4px_8px_rgba(0,0,0,0.1)] rounded-[10px]">
                <h2 style={{ WebkitTextFillColor: "#000" }} className={`${playfair.className} text-center text-4xl font-bold mb-6 text-black`}>Buffet Menu</h2>

                {/* mobile-first grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 w-full">
                {buffetCategories.map((category) => (
                    <div key={category} className={orderMap[category]}>
                    <BuffetCategory
                        category={category}
                        subtitle={subtitleFor(category)}
                        items={buffetItems.filter((i) => i.category === category)}
                        onClick={toggleModal}
                    />
                    </div>
                ))}
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
