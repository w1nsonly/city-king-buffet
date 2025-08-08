import Header from "@/components/common/Header";
import HomeBody from "@/components/sections/HomeSection";
import BuffetItems from "../components/sections/BuffetSection";
import MenuItems from "../components/sections/MenuSection";
import QuestionPage from "../components/sections/QuestionSection";
import Footer from "@/components/common/Footer";

export default function Home() {
  
  return (
    <>
      <Header />
        <section id="home">
          <HomeBody />
        </section>

        <section id="buffet">
          <BuffetItems />
        </section>

        <section id="menu">
          <MenuItems />
        </section>

        <section id="question">
          <QuestionPage />
        </section>
      <Footer />
    </>  
  );
}
