// components/menu/BuffetCategory.tsx

import { BuffetItemTypes } from "@/types";
import { Playfair_Display } from "next/font/google";

const playfair = Playfair_Display({
  subsets: ["latin"],
});

interface BuffetProps {
    category: string;
    subtitle?: string;
    items: BuffetItemTypes[];
    onClick: (item: BuffetItemTypes) => void;
}

export default function BuffetCategory({ category, subtitle, items, onClick }: BuffetProps) {

    return (
    <div className="mb-6 w-full">
       <h3 style={{ WebkitTextFillColor: "#000" }} className="text-2xl text-black font-bold mb-2">
            <span className={`${playfair.className} border-b-2 border-[#830e0e]`}>
                {category}
            </span>
        </h3>

        {subtitle ? (
            <p style={{ WebkitTextFillColor: "#000" }} className="text-sm text-black-600 italic mb-1">{subtitle}</p>
        ) : null}
        
        <ul className="w-full">
            {items.map((item) => (
                <li
                key={item.name}
                onClick={() => onClick(item)}
                style={{ WebkitTextFillColor: "#000" }}
                className={`
                    ${playfair.className}
                    p-2.5 border-b border-gray-200
                    flex items-center justify-between gap-3
                    text-base md:text-lg text-black-700 
                    hover:bg-red-100 last:border-0
                    min-w-0
                    `
                }
                >
                {/* name wraps, can shrink */}
                <span className="flex-1 min-w-0 break-words">
                    {item.name}
                </span>
                {/* price stays compact, never wraps/shrinks */}
                <span className="shrink-0 whitespace-nowrap pl-3 font-bold text-red-600 tabular-nums">
                    ${Number(item.price).toFixed(2)}
                </span>
                </li>
            ))}
        </ul>
    </div>
    );
}
