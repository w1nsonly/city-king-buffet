


export function Header() {

    return (
        <header className="bg-[#830e0e] px-[2%] py-[1%] text-[bisque] text-2xl justify-between items-center">
            <div className="flex justify-between">
                <h1>City King Buffet</h1>
                <nav>
                    <ul className="flex flex-row space-x-5">
                        <li><a href="/">Home</a></li>
                        <li><a href="/buffet">Buffet</a></li>
                        <li><a href="/menu">Menu</a></li>
                        <li><a href="/question">Question</a></li>
                    </ul>
                </nav>
            </div>
        </header>

    )

}