import styles from "./HomeSection.module.css";

export default function HomeSection() {

  return (
    <main>
      <div className="flex flex-col items-center justify-center gap-35 w-full h-150 bg-[url('/citykingbuffet1.jpg')] bg-cover bg-center bg-no-repeat">
        <h2  className="text-center text-[calc(4px+3.5vw)] text-white font-bold mb-[4%] opacity-0 animate-[arcIn_1.4s_ease-out_forwards]">
          City King Buffet
        </h2>

        {/* Three main cards */}
        <div className="flex flex-row justify-center items-center gap-5">
          {/* Buffet Card*/}
          <div className={styles.card}>
            <h3 className={styles.cardTitle}>Buffet</h3>
              <p className={styles.cardText}>
                Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Quibusdam, modi diuagwiudgawid !
              </p>
          </div>

          {/* Hibachi Card */}
          <div className={styles.card}>
            <h3 className={styles.cardTitle}>Hibachi</h3>
              <p className={styles.cardText}>
                Sizzling grilled meats, seafood, and veggies cooked right in front
                of you.
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
      <br />
    </main>
  );
}
