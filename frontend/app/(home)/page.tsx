// app/(home)/page.tsx

import HomeSection from "./components/HomeSection/HomeSection";
import BuffetSection from "./components/BuffetSection/BuffetSection";
import QuestionSection from "./components/QuestionSection/QuestionSection";

export default function Home() {
    
    return (
        <>
            <HomeSection />
            <BuffetSection />
            <QuestionSection />
        </>
    );
}

