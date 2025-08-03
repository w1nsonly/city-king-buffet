// ChatBox.tsx
"use client"
import { useState, useEffect, useRef } from "react"
import ChatForm, { ChatMessageType } from "./ChatForm";
import ChatMessage from "./ChatMessage";

export default function ChatBox() {
    const [chatHistory, setChatHistory] = useState<ChatMessageType[]>([])
   

    // Handle auto-scroll when messages arrive
    

    return (
       <div className="chatbox-container max-w-2xl mx-auto bg-white rounded-lg shadow-lg border border-red-200 overflow-hidden">
            
            {/* ChatBox Messages */}
            <div className="chat-messages h-96 overflow-y-auto p-4 space-y-4 bg-red-50">
                <div className="AI Chat flex justify-start">
                    <div className="bg-white border border-red-200 rounded-2xl rounded-bl-md px-4 py-2 max-w-xs shadow-sm">
                        <p className="text-red-900 text-sm">Hello, how could I help you?</p>
                    </div>
                </div> 

                {/* now render each saved message as its own row */}
                {chatHistory.map((chat, idx) => (
                <div key={idx} className={`flex ${chat.role === "user" ? "justify-end" : "justify-start"}`}>
                    <ChatMessage chat={chat} />
                </div>
                ))}
            </div>
            
            {/* ChatBox Input */}
            <div className="chat-input border-t border-red-200 p-4 bg-white">
                <ChatForm setChatHistory={setChatHistory} />
            </div>

        </div>
    )
}