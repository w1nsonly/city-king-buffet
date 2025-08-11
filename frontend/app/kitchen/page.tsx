// app/kitchen/page.tsx

'use client'
import React, { useState, useEffect } from "react";
import axios from "axios";
import KitchenCategory from "@/components/menu/KitchenCategory";
import { KitchenItem } from "@/types";
import ItemModal from "@/components/modal/ItemModal";
import { Playfair_Display } from "next/font/google";

const playfair = Playfair_Display({
  subsets: ["latin"],
});

import Header from "@/components/common/Header";
import Footer from "@/components/common/Footer";
import Link from "next/link";

export default function KitchenMenu() {
    const API_BASE = process.env.NEXT_PUBLIC_API_BASE!;
    const [kitchenItems, setKitchenItems] = useState<KitchenItem[]>([]);
    const [modal, setModal] = useState(false);
    const [selectedItem, setSelectedItem] = useState<KitchenItem| null>(null);

    function toggleModal(item?: KitchenItem) {
        if (modal) {
            setSelectedItem(null);
        } else if (item) {
            setSelectedItem(item);
        }
        setModal(!modal)
    }

    useEffect(() => {
    axios
        .get<KitchenItem[]>(`${API_BASE}restaurant/menu/regular`)
        .then((res) => setKitchenItems(res.data))
        .catch((err) => console.error("Error fetching menu:", err));
    }, []);

  return (
    <>
        <Header />
        {/* page wrapper */}
        <div className="w-full overflow-x-hidden bg-[url('/lightbeige.jpg')] py-10">
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
                            <KitchenCategory
                                key={category}
                                category={category}
                                items={kitchenItems.filter((i) => i.category === category)}
                                onClick={toggleModal}
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
                            <KitchenCategory
                                key={category}
                                category={category}
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
        <Footer />
    </>
  );
}
