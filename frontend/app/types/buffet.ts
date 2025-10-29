// app/types/buffet.ts

export interface BuffetCategoryTypes {
    id: number;
    name: string;
    subtitle: string;
}

export interface BuffetItemTypes {
    id: number;
    name: string;
    price: string;
    category: string;
}

