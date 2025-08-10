// components/sections/HomeSection.tsx

import styles from "./HomeSection.module.css";

export default function HomeSection() {

    return (

        <section id="home" className="flex flex-col items-center justify-start w-full min-h-screen pt-10 sm:pt-20 gap-6 sm:gap-40 bg-[url('/citykingbuffet1.jpg')] bg-cover bg-center bg-no-repeat px-4">
            <h2 className="text-center text-[calc(15px+3.5vw)] sm:text-[calc(4px+3.5vw)] text-white font-bold mb-[4%] opacity-0 animate-[arcIn_1.4s_ease-out_forwards]">
                City King Buffet
            </h2>

            {/* Cards */}
            <div className="flex flex-col items-center gap-6 pb-5 sm:pb-10 sm:flex-row sm:justify-center sm:gap-10 w-full max-w-[1000px] sm:mt-6">
                <div className={styles.card}>
                    <h3 className={styles.cardTitle}>Buffet</h3>
                        <p className={styles.cardText}>
                            Endless fresh flavors, all in a lively all-you-can-eat experience.
                        </p>
                </div>

                <div className={styles.card}>
                    <h3 className={styles.cardTitle}>Hibachi</h3>
                        <p className={styles.cardText}>
                            Fresh meats, seafood, and veggies grilled to perfection right before your eyes.
                        </p>
                </div>

                <div className={styles.card}>
                    <h3 className={styles.cardTitle}>Sushi</h3>
                        <p className={styles.cardText}>
                            Fresh, handcrafted sushi rolls with a perfect balance of flavors.
                        </p>
                </div>
            </div>
        </section>
    );
}
