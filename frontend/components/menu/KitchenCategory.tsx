// components/menu/KitchenCategory.tsx

import { KitchenItem } from "@/types";
import { Playfair_Display } from "next/font/google";

const playfair = Playfair_Display({
  subsets: ["latin"],
});

interface KitchenProps {
    category: string;
    items: KitchenItem[];
    onClick: (item: KitchenItem) => void;
}

export default function KitchenCategory({ category, items, onClick }: KitchenProps) {

  return (
    <div className="mb-6 w-full">
       <h3 className={`${playfair.className} font-bold text-2xl mb-2 text-black [-webkit-text-fill-color:#000]`}>{category}</h3>
        <ul className="list-none p-0 m-0 w-full">
            {items.map((item) => (
                <li
                key={item.id_number ?? item.name}
                onClick={() => onClick(item)}
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
                    {item.id_number ? `${item.id_number}. ` : ""}
                    {item.name}
                </span>
                {/* price stays compact */}
                <span className="shrink-0 whitespace-nowrap pl-3 font-bold text-red-600 tabular-nums">
                    ${Number(item.price).toFixed(2)}
                </span>
                </li>
            ))}
        </ul>
    </div>
    );
}
