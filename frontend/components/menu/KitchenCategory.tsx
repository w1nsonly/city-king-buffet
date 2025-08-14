// components/menu/KitchenCategory.tsx

import { KitchenItemTypes } from "@/types";
import { Playfair_Display } from "next/font/google";
import Image from "next/image";

const playfair = Playfair_Display({
  subsets: ["latin"],
});

interface KitchenProps {
    category: string;
    subtitle?: string; // optional
    items: KitchenItemTypes[];
    onClick: (item: KitchenItemTypes) => void;
}

export default function KitchenCategory({ category, subtitle, items, onClick }: KitchenProps) {


  return (
    <div className="mb-6 w-full">
        <h3 style={{ WebkitTextFillColor: "#000" }} className="text-2xl font-bold mb-2">
            <span className={`${playfair.className} border-b-2 border-[#830e0e]`}>
                {category}
            </span>
        </h3>
        
        {subtitle ? (
            <p style={{ WebkitTextFillColor: "#000" }} className="text-sm italic mb-1">{subtitle}</p>
        ) : null}

        <ul className="list-none p-0 m-0 w-full">
            {items.map((item) => (
                <li
                key={item.id_number ?? item.name}
                onClick={() => onClick(item)}
                style={{ WebkitTextFillColor: "#000" }}
                className={`
                    ${playfair.className}
                    p-2.5 border-b border-gray-200
                    flex items-center justify-between gap-3
                    text-base md:text-lg hover:bg-red-100 
                    last:border-0 min-w-0
                    `
                }
                >
                {/* name wraps, can shrink */}
                <span className="flex-1 min-w-0 break-words">
                    {item.id_number ? `${item.id_number}. ` : ""}
                    {item.name}
                    {item.is_spicy && (
                        <Image
                            width={24}
                            height={24}
                            src="/spicy-flame.svg"
                            alt="Spicy"
                            className="absolute ml-2 inline-block align-[-0.125rem]"
                            loading="lazy"
                        />
                    )}
                </span>
                {/* price stays compact */}
                <span className="shrink-0 whitespace-nowrap pl-3 font-bold tabular-nums">
                    ${Number(item.price).toFixed(2)}
                </span>
                </li>
            ))}
        </ul>
        
    </div>
    );
}
