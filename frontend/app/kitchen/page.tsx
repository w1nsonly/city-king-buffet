// app/kitchen/page.tsx

'use client'
import React, { useState, useEffect } from "react";
import axios from "axios";
import KitchenCategory from "./components/KitchenCategory";
import { KitchenCategoryTypes, KitchenItemTypes } from "@/app/types";
import ItemModal from "@/app/components/modal/ItemModal";
import Link from "next/link";

import { Playfair_Display } from "next/font/google";
const playfair = Playfair_Display({
    subsets: ["latin"],
});

export default function KitchenMenu() {
    
    const API_BASE = process.env.NEXT_PUBLIC_API_BASE!;
    const [modal, setModal] = useState(false);
    const [kitchenItems, setKitchenItems] = useState<KitchenItemTypes[]>([]);
    const [selectedItem, setSelectedItem] = useState<KitchenItemTypes | null>(null);
    const [categoriesMeta, setCategoriesMeta] = useState<KitchenCategoryTypes[]>([]);


    function toggleModal(item?: KitchenItemTypes) {
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
                    axios.get<KitchenItemTypes[]>(`${API_BASE}restaurant/menu/kitchen`),
                    axios.get<KitchenCategoryTypes[]>(`${API_BASE}restaurant/category/kitchen`),
                ]);
                setKitchenItems(itemsRes.data);
                setCategoriesMeta(catsRes.data);
            } catch (err) {
                console.error("Error fetching kitchen data:", err);
            }
        })();
    }, [API_BASE]);

    const subtitleFor = (name: string) =>
        categoriesMeta.find(c => c.name === name)?.subtitle || "";

    const left = [
        "Appetizers","Soups","Chow Mein","Chop Suey","Lo Mein","Mei Fun",
        "Fried Rice","Egg Foo Young","Vegetable","Shrimp","Beef","Pork","Chicken",
    ];
    const right = ["Lunch Combos","Special Combos","Chef Specials","Diet Menu","Sushi Rolls","Side Orders"];

    return (
    <>
        {/* page wrapper */}
        <div className="w-full overflow-x-hidden bg-[url('/images/light-beige.jpg')] py-10">
            {/* top bar w/ back link */}
            <div className="w-full max-w-[1000px] mx-auto px-4 sm:px-6">
            <Link href="/#home" className="inline-flex items-center gap-2 px-4 py-2 bg-[#830e0e] text-[bisque] rounded-full shadow-md transition-all duration-200 hover:text-white hover:bg-[#a83232]">
                <span className="text-lg">←</span> Back to Buffet
            </Link>
            </div>

            {/* card container */}
            <div className="mt-4 w-full max-w-[1000px] mx-auto px-4 sm:px-6">
                <div className="p-5 bg-[#fffdf5] shadow-[0_4px_8px_rgba(0,0,0,0.1)] rounded-[10px]">
                    <h2 style={{ WebkitTextFillColor: "#000" }} className={`${playfair.className} text-center text-4xl font-bold mb-6 text-black`}>Kitchen Menu</h2>

                    {/* mobile-first grid */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                        {/* Left column */}
                        <div className="flex flex-col gap-5">
                            {left.map((category) => (
                            <KitchenCategory
                                key={category}
                                category={category}
                                subtitle={subtitleFor(category)}
                                items={kitchenItems.filter((i) => i.category === category)}
                                onClick={toggleModal}
                            />
                            ))}
                        </div>

                        {/* Right column */}
                        <div className="flex flex-col gap-5">
                            {right.map((category) => (
                            <KitchenCategory
                                key={category}
                                category={category}
                                subtitle={subtitleFor(category)}
                                items={kitchenItems.filter((i) => i.category === category)}
                                onClick={toggleModal}
                            />
                            ))}
                        </div>
                    </div>
                    {selectedItem && (
                        <ItemModal modal={modal} toggleModal={toggleModal} item={selectedItem} price={Number(selectedItem.price)}/>
                    )}
                </div>
            </div>
        </div>
    </>
  );
}
