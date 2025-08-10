// components/ChatBox/ChatForm.tsx

"use client"
import { Dispatch, SetStateAction, useRef, FormEvent } from 'react'

// 1) Define message shape
export type ChatMessageType = { role: "user" | "model"; text: string };

// 2) Define the props shape for ChatForm
interface ChatFormProps {                          
    setChatHistory: Dispatch<SetStateAction<ChatMessageType[]>>; // setter
    generateAIResponse: (history: ChatMessageType[]) => void;    //custom callback
}

export default function ChatForm({ setChatHistory, generateAIResponse } : ChatFormProps ) {

    const inputRef = useRef<HTMLInputElement>(null)

    
    const handleFormSubmit = (e: FormEvent<HTMLFormElement>): void => {
        e.preventDefault();
        const userMessage = inputRef.current?.value.trim();
        if (!userMessage) return;
        inputRef.current!.value = "";

        // 1) Pure state update: no side-effects here
        let next: ChatMessageType[] = [];
        setChatHistory(prev => {
            next = [...prev, { role: "user", text: userMessage }];
            return next;
        });

        // 2) Side-effects AFTER state update (won’t double in StrictMode)
        setTimeout(() => {
            setChatHistory(h => [...h, { role: "model", text: "Thinking..." }]);
            generateAIResponse(next);
        }, 600);
    };
    
    return (
        <form action="#" className="flex items-center gap-3 w-full" onSubmit={handleFormSubmit}>
            <input 
            ref={inputRef}
            type="text" 
            placeholder="Your message here..." 
            className="message-input flex-1 min-w-0 px-4 py-2 border border-red-300 rounded-full focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent resize-none" 
            required
            />

            <button className="bg-red-600 hover:bg-red-700 text-white px-6 py-2 rounded-full transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">
                Send
            </button>
        </form>
            
    )
}