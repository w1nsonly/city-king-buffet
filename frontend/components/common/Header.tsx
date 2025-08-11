// components/common/Header.tsx

import { Playfair_Display } from "next/font/google";
import Link from "next/link";

const playfair = Playfair_Display({ subsets: ["latin"] });

export default function Header() {

    return (
        <header className="sticky top-0 z-50 bg-[#830e0e] text-[bisque]">
            <div className="mx-auto w-full max-w-[1000px] px-4 sm:px-6 py-3 flex items-center justify-between">
                <h1 className={`${playfair.className} font-700 text-xl sm:text-4xl`}>City King Buffet</h1>
                <nav className="text-base sm:text-xl">
                    <ul className="flex flex-row gap-4 sm:gap-6">
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
    );
}
