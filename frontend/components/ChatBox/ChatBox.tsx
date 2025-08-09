// components/ChatBox/ChatBox.tsx

"use client"
import { useState, useEffect, useRef } from "react"
import ChatForm, { ChatMessageType } from "./ChatForm";
import ChatMessage from "./ChatMessage";

export default function ChatBox() {
    const [chatHistory, setChatHistory] = useState<ChatMessageType[]>([])
    const chatRef = useRef<HTMLDivElement | null>(null)

    
    const generateAIResponse = async (history: ChatMessageType[]) => {
        // Get the latest user message
        const latestMessage = history[history.length - 1];
        if (latestMessage.role !== "user") return;

        const url = `http://127.0.0.1:8000/restaurant/chat?q=${encodeURIComponent(latestMessage.text)}`;
        console.log("Calling URL:", url);

        try {
            const response = await fetch(url);
            console.log("Response status:", response.status);
            console.log("Response ok:", response.ok);
            
            const data = await response.json();
            console.log("Response data:", data);
            
            if (response.ok && data.answer) {
                // Replace the "Thinking..." message with the actual AI response
                setChatHistory(prevHistory => {
                    const newHistory = [...prevHistory];
                    // Find the last "Thinking..." message and replace it
                    for (let i = newHistory.length - 1; i >= 0; i--) {
                        if (newHistory[i].role === "model" && newHistory[i].text === "Thinking...") {
                            newHistory[i].text = data.answer;
                            break;
                        }
                    }
                    return newHistory;
                });
            } 
        } catch (error) {
            console.error("Fetch error:", error);
            // Replace "Thinking..." with error message
            setChatHistory(prevHistory => {
                const newHistory = [...prevHistory];
                for (let i = newHistory.length - 1; i >= 0; i--) {
                    if (newHistory[i].role === "model" && newHistory[i].text === "Thinking...") {
                        newHistory[i].text = "Something went wrong!";
                        break;
                    }
                }
                return newHistory;
            });
        }
    };

    const askQuestion = (question: string): void => {

        let next: ChatMessageType[] = [];
        setChatHistory(prev => {
            next = [...prev, { role: "user", text: question }];
            return next;
        });

        // side-effects OUTSIDE the updater (won’t double in StrictMode)
        setTimeout(() => {
            setChatHistory(h => [...h, { role: "model", text: "Thinking..." }]);
            generateAIResponse(next);
        }, 600);
    };

    useEffect(() => {
        // Auto-scroll whenever chat history updates
        if (!chatRef.current) return
        chatRef.current.scrollTo({top: chatRef.current.scrollHeight, behavior: "smooth"});
    },[chatHistory]);
    
    return (
        <div className="chatbox-container max-w-2xl mx-auto bg-white rounded-lg shadow-lg border border-red-200 overflow-hidden">
            {/* ChatBox Messages */}
            <div ref={chatRef} className="chat-messages h-96 overflow-y-auto p-4 space-y-4 bg-red-50">
                <div className="AI Chat flex justify-start">
                    <div className="bg-white border border-red-200 rounded-2xl rounded-bl-md px-4 py-2 max-w-xs shadow-sm">
                        <p className="text-red-900 text-sm">Hello, how could I help you?</p>
                    </div>
                </div> 

                {/* now render each saved message as its own row */}
                {chatHistory.map((chat, idx) => (
                <div key={idx} className={`flex ${chat.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <ChatMessage chat={chat} />
                </div>
                ))}

            </div>
            
            {/* ChatBox Input */}
            <div className="chat-input border-t border-red-200 p-4 bg-white">
                <div className="grid grid-cols-1 md:grid-cols-[auto,1fr] md:items-center md:gap-4">
                    {/* Quick buttons: stack centered on mobile, left-docked on desktop */}
                    <div className="order-1 md:order-none mb-3 md:mb-0 flex justify-center md:justify-start gap-2">
                        <button type="button" onClick={() => askQuestion("How much is it right now?")} className="inline-flex items-center gap-2 rounded-full px-4 py-2 bg-red-600 text-white shadow-sm hover:bg-red-700 active:scale-[0.98] focus:outline-none focus-visible:ring-2 focus-visible:ring-red-500">
                            Price Today
                        </button>
                        <button type="button" onClick={() => askQuestion("What are your hours today?")} className="inline-flex items-center gap-2 rounded-full px-4 py-2 bg-white text-red-700 border border-red-300 shadow-sm hover:bg-red-50 active:scale-[0.98] focus:outline-none focus-visible:ring-2 focus-visible:ring-red-500">
                            Hours Today
                        </button>
                    </div>
                    {/* Input + Send occupies the right column on desktop / full width on mobile */}
                    <ChatForm setChatHistory={setChatHistory} generateAIResponse={generateAIResponse} />
                </div>
            </div>
        </div>
    )
}