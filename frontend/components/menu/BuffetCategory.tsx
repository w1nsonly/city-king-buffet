// components/menu/BuffetCategory.tsx

import { BuffetItem } from "@/types";

interface BuffetProps {
    category: string;
    items: BuffetItem[];
    onClick: (item: BuffetItem) => void;
}

export default function BuffetCategory({ category, items, onClick }: BuffetProps) {

    return (
    <div className="mb-6 w-full">
        <h3 className="text-xl font-semibold mb-2">{category}</h3>
        <ul className="w-full">
            {items.map((item) => (
                <li
                key={item.name}
                onClick={() => onClick(item)}
                className="
                    p-2.5 border-b border-gray-200
                    flex items-center justify-between gap-3
                    text-base md:text-lg text-gray-700
                    hover:bg-red-100 last:border-0
                    min-w-0
                "
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
