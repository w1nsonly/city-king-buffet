// app/types/kitchen.ts

export interface KitchenCategoryTypes {
    id: number;
    name: string;
    subtitle: string;
}

export interface KitchenItemTypes {
    id: number;
    category: string;
    id_number: string;
    name: string;
    price: string;
    is_spicy: boolean;
}

