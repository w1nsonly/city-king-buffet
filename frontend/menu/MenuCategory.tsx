import { MenuItem } from "@/types";

interface MenuProps {
  category: string;
  items: MenuItem[]
}

export default function MenuCategory({ category, items}: MenuProps) {
  
  return (

    <div className="mb-6">
      <h3 className="text-xl font-semibold mb-2">{category}</h3>
      <ul className="list-none p-0 m-0">
        {items.map((item) => (
          <li key={item.id_number ?? item.name}
            className="
              p-2.5 
              border-b border-gray-200 
              flex justify-between items-center 
              text-lg text-gray-700 
              hover:bg-red-100 
              last:border-0 
              cursor-pointer
            "
            >
            <span>
              {item.id_number ? `${item.id_number}. ` : ""}
              {item.name}
            </span>
            <span className="font-bold text-red-600">
              ${item.price}
            </span>
          </li>
        ))}
      </ul>
    </div>

  );
}
