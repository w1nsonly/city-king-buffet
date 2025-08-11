// components/sections/QuestionSection/ChatBox/ChatMessage.tsx

"use client"
import React from "react"
import type { ChatMessageType } from "./ChatForm"

interface ChatMessageProps {
    chat: ChatMessageType
}

export default function ChatMessage({ chat } : ChatMessageProps) {
    const isUser = chat.role === "user"
    
    return (
        <div className={isUser ? "User Chat flex justify-end" : "AI Chat flex justify-start"}>
            <div className={isUser ? "bg-red-600 text-white rounded-2xl rounded-br-md px-4 py-2 max-w-[80%] md:max-w-xs shadow-sm" : "bg-white border border-red-200 rounded-2xl rounded-bl-md px-4 py-2 max-w-[80%] md:max-w-xs shadow-sm"}>
                <p className={isUser ? "text-sm break-words" : "text-red-900 text-sm break-words"}>
                    {chat.text}
                </p>
            </div>
        </div>
    )
}