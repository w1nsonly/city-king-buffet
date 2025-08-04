'use client'
import ChatBox from "@/components/ChatBox"

export default function QuestionPage() {

    return (
        <div className="min-h-screen bg-gray-50 py-12">
            <h2 className="text-3xl font-bold text-center mb-6">
                Ask City King Buffet
            </h2>
            <ChatBox />
        </div>
    )
}