import styles from "./HomeSection.module.css";

export default function HomeSection() {

  return (
    <main>
      <div className="flex flex-col items-center justify-center gap-60 w-full h-180 bg-[url('/citykingbuffet1.jpg')] bg-cover bg-center bg-no-repeat">
        <h2  className="text-center text-[calc(4px+3.5vw)] text-white font-bold mb-[4%] opacity-0 animate-[arcIn_1.4s_ease-out_forwards]">
          City King Buffet
        </h2>

        {/* Three main cards */}
        <div className="flex flex-row justify-center items-center gap-5">
          {/* Buffet Card*/}
          <div className={styles.card}>
            <h3 className={styles.cardTitle}>Buffet</h3>
              <p className={styles.cardText}>
                Endless fresh flavors, all in a lively all-you-can-eat experience.
              </p>
          </div>

          {/* Hibachi Card */}
          <div className={styles.card}>
            <h3 className={styles.cardTitle}>Hibachi</h3>
              <p className={styles.cardText}>
                Fresh meats, seafood, and veggies grilled to perfection right before your eyes.
              </p>
          </div>

          {/* Sushi Card */}
          <div className={styles.card}>
            <h3 className={styles.cardTitle}>Sushi</h3>
              <p className={styles.cardText}>
                Fresh, handcrafted sushi rolls with a perfect balance of flavors.
              </p>
          </div>
        </div>
      </div>
    </main>
  );
}
