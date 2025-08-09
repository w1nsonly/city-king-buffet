// components/menu/BuffetCategory.tsx

import { BuffetItem } from "@/types";

interface BuffetProps {
    category: string;
    items: BuffetItem[];
}

export default function BuffetCategory({category, items} : BuffetProps) {

    return (

        <div className="mb-6">
            <h3 className="text-xl font-semibold mb-2">{category}</h3>
            <ul>
                {items.map((item) => (
                    <li key={item.name} 
                        className="
                        p-2.5 
                        border-b border-gray-200 
                        flex justify-between items-center 
                        text-lg text-gray-700 
                        hover:bg-red-100 
                        last:border-0 
                        "
                        >
                        <span>
                            {item.name}
                        </span>
                        <span className="font-bold text-red-600">
                            {item.price}
                        </span>
                    </li>
                ))}
            </ul>
        </div>


    )

}