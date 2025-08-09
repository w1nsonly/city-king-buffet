// components/common/Header.tsx

import { Playfair_Display } from "next/font/google";
import Link from "next/link";

const playfair = Playfair_Display({ subsets: ["latin"], weight: ["700"] });


export default function Header() {

    return (
        <header className="sticky top-0 z-50 bg-[#830e0e] px-[2%] py-[1%] text-[bisque] text-2xl justify-between items-center">
            <div className="flex justify-between items-center max-w-[1000px] mx-auto">
                <h1 className={`${playfair.className} text-2xl`}>City King Buffet</h1>
                <nav className="text-lg font-['Avenir_Light','avenir-lt-w01-35-light1475496',sans-serif] font-light">
                    <ul className="flex flex-row space-x-5">
                        {[
                        { name: "Home", href: "/#home" },
                        { name: "Buffet", href: "/#buffet" },
                        { name: "Question", href: "/#question" },
                        { name: "Kitchen", href: "/kitchen" },
                        ].map((link) => (
                        <li key={link.name}>
                            <Link href={link.href} className="hover:text-white hover:underline underline-offset-4">
                            {link.name}
                            </Link>
                        </li>
                        ))}
                    </ul>
                </nav>
            </div>
        </header>

    )

}