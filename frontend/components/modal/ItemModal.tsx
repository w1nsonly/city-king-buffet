// components/modal/ItemModal.tsx

import { useEffect } from "react";
import { BuffetItem, KitchenItem } from "@/types";
import "./ItemModal.css";

interface ItemModalProps {
    modal: boolean;
    toggleModal: () => void;
    item: BuffetItem | KitchenItem;
    price: number;
}

export default function ItemModal({ modal, toggleModal, item }: ItemModalProps) {

    useEffect(() => {
        if (modal) {
            document.body.classList.add("active-modal");
        } else {
            document.body.classList.remove("active-modal")
        }

        return () => document.body.classList.remove("active-modal");
    }, [modal]);


    return (
        <>
            {modal && (
                <div className="modal">
                    <div className="overlay" onClick={toggleModal}></div>
                    <div className="modal-content">
                        <div className="item-wrapper">
                            <h2>{item.name}</h2>
                            <p>${Number(item.price).toFixed(2)}</p>
                        </div>
                        <button className="close-button" onClick={toggleModal}>
                            <img src="/close-icon.png" alt="X Close Button Icon" />
                        </button>
                    </div>
                </div>
            )}
        </>
    )
}