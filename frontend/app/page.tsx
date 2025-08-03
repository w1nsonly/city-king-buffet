export default function Home() {

  return (
      <div id="container">
        <main>
          <div className="flex flex-col items-center">
              <h2 className="text-center text-[calc(4px+2.5vw)] font-bold mb-[4%]">Welcome to City King Buffet!</h2>
              <img 
              src="citykingbuffet.jpg" 
              alt="City King Buffet"
              className="
                w-1/2 
                h-auto 
                rounded-[10%] 
                shadow-[0px_calc(2px+0.3vw)_calc(6px+0.5vw)_black 
                transition-all 
                duration-300 ease-in-out 
                mb-[3vh]"
              />
          </div>
          <div>
            <div>
              <h3>Buffet</h3>
              <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam, modi!</p>
            </div>
            <div>
              <h3>Hibachi</h3>
              <p>Sizzling grilled meats, seafood, and veggies cooked right in front of you.</p>
            </div>
            <div>
              <h3>Sushi</h3>
              <p>Fresh, handcrafted sushi rolls with a perfect balance of flavors.</p>
            </div>
          </div>
          <br />
          
          <div>
            <p>Got a question? <a href="/question">Click Here!</a></p>
          </div>
        </main>
      </div>
  )
}
