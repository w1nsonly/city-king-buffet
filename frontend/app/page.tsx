// app/page.tsx

import Header from "@/components/common/Header";
import HomeSection from "@/components/sections/HomeSection/HomeSection";
import BuffetSection from "@/components/sections/BuffetSection/BuffetSection";
import QuestionSection from "@/components/sections/QuestionSection/QuestionSection";
import Footer from "@/components/common/Footer";

export default function Home() {
    
    return (
        <>
            <main>
                <Header />
                <HomeSection />
                <BuffetSection />
                <QuestionSection />
                <Footer />
            </main>
        </>
    );
}
