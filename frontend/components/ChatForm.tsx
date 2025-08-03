// ChatForm.tsx
"use client"
import React, { useRef, FormEvent } from 'react'

// 1) Define message shape
export type ChatMessageType = { role: "user" | "model"; text: string };

// 2) Define the props shape for ChatForm
interface ChatFormProps {
  setChatHistory: React.Dispatch<React.SetStateAction<ChatMessageType[]>>;
}

export default function ChatForm({ setChatHistory } : ChatFormProps ) {
    const inputRef = useRef<HTMLInputElement>(null)

    const handleFormSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()
        const userMessage = inputRef.current?.value.trim()
        if (!userMessage) return
        inputRef.current!.value = ''

        // Update chat history with the user's message
        setChatHistory(history => [...history, { role: "user", text: userMessage}])

        // Update chat history with the user's message
       setTimeout(() => setChatHistory(history => [...history,{ role: "model", text: "Thinking..." }]),600)
    }
    
    return (
        <form action="#" className="flex items-center gap-3 w-full" onSubmit={handleFormSubmit}>
            <input 
                ref={inputRef}
                type="text" 
                placeholder="Your message here..." 
                className="message-input flex-1 px-4 py-2 border border-red-300 rounded-full focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent resize-none" 
                required
            />
            <button className="bg-red-600 hover:bg-red-700 text-white px-6 py-2 rounded-full transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2">
                Send
            </button>
        </form>
            
    )
}