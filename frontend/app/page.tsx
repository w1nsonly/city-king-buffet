// app/page.tsx

import Header from "@/components/common/Header";
import HomeSection from "@/components/sections/HomeSection";
import BuffetSection from "@/components/sections/BuffetSection";
import QuestionSection from "@/components/sections/QuestionSection";
import Footer from "@/components/common/Footer";


export default function Home() {
  
  return (
    <>
      <main>
        <Header />
          <section id="home">
            <HomeSection />
          </section>

          <section id="buffet">
            <BuffetSection />
          </section>
          
          <section id="question">
            <QuestionSection />
          </section>
        <Footer />
      </main>
    </>  
  );
}
