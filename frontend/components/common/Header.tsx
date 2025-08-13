// components/common/Header.tsx

'use client'
import { Playfair_Display } from "next/font/google";
import { Squash as Hamburger } from 'hamburger-react'
import Link from "next/link";
import Image from "next/image";
import { useState } from "react";


const playfair = Playfair_Display({ subsets: ["latin"] });

const links = [
  { name: "Home", href: "/#home" },
  { name: "Buffet", href: "/#buffet" },
  { name: "Question", href: "/#question" },
  { name: "Kitchen", href: "/kitchen" },
];


export default function Header() {
    const [isOpen, setOpen] = useState(false);

    return (
        <header className="sticky top-0 z-50 bg-[#830e0e] text-[bisque]">
            <div className="mx-auto w-full max-w-[1000px] px-4 sm:px-6 py-3 flex items-center justify-between">
                <Link href="/#home" className="flex items-center gap-2 sm:gap-3">
                    <div className="relative h-10 w-10 sm:h-10 sm:w-10 overflow-visible translate-x-1 sm:translate-x-0">
                        <Image 
                            src="city-king-crown.svg" 
                            alt="City King" fill 
                            className="object-contain transform scale-200 sm:scale-150 origin-center" 
                            priority 
                        />
                    </div>
                    <h1 className={`${playfair.className} hidden sm:block font-700 text-xl sm:text-4xl`}>
                        City King Buffet
                    </h1>
                </Link>

                {/* Desktop nav */}
                <nav className="hidden sm:block text-xl">
                    <ul className="flex flex-row gap-6">
                    {links.map((link) => (
                        <li key={link.name}>
                            <Link href={link.href} className="hover:text-white hover:underline underline-offset-4">
                                {link.name}
                            </Link>
                        </li>
                    ))}
                    </ul>
                </nav>

                {/* Hamburger button (mobile) */}
                <div className="sm:hidden">
                    <Hamburger toggled={isOpen} toggle={setOpen} easing="ease-in" rounded />

                    {isOpen && (
                        <>
                            {/* click-away overlay */}
                            <button
                                aria-label="Close menu"
                                className="fixed inset-0 z-40 cursor-default"
                                onClick={() => setOpen(false)}
                            />

                            {/* dropdown panel */}
                            <nav className="absolute right-2 mt-3 z-50 w-35 rounded-md bg-[#fffdf5] text-[black] text-center shadow-[0_4px_8px_rgba(0,0,0,0.1)]">
                                <ul className="py-2">
                                {links.map(link => (
                                    <li key={link.name}>
                                        <Link href={link.href} onClick={() => setOpen(false)} className="block px-4 py-2 text-lg">
                                            {link.name}
                                        </Link>
                                    </li>
                                ))}
                                </ul>
                            </nav>
                        </>

                    )}
                </div>
            </div>
        </header>

    );
}
