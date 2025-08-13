// components/sections/QuestionSection/QuestionSection.tsx

'use client'
import ChatBox from "@/components/sections/QuestionSection/ChatBox/ChatBox"

export default function QuestionSection() {

    return (
        <section id="question" className="min-h-screen bg-gray-50 py-12 bg-[url('/city-king-buffet-2.jpg')] bg-cover bg-center bg-no-repeat">
            <div className="w-full max-w-[1000px] mx-auto px-4">
                <h2 className="text-3xl font-bold text-white text-center mb-6">
                    Ask City King Buffet
                </h2>
                <ChatBox />
            </div>
        </section>
    )
}