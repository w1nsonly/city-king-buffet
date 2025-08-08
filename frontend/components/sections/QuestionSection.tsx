'use client'
import ChatBox from "@/components/ChatBox/ChatBox"

export default function QuestionSection() {

    return (
        <div className="min-h-screen bg-gray-50 py-12 bg-[url('/citykingbuffet2.jpg')] bg-cover bg-center bg-no-repeat">
            <h2 className="text-3xl font-bold text-white text-center mb-6">
                Ask City King Buffet
            </h2>
            <ChatBox />
        </div>
    )
}