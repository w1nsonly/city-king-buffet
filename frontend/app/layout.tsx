// app/layout.tsx

import type { Metadata } from "next";
import React from "react";
import "./globals.css";
import Header from "@/app/components/layout/Header";
import Footer from "@/app/components/layout/Footer";

export const metadata: Metadata = {
  title: "City King Buffet",
  description: "City King Buffet - Explore our buffet menu, kitchen, and get instant answers to your questions with our AI-powered chatbox.",
};

export const viewport = {
  width: 'device-width',
  initialScale: 1,
};

export default function RootLayout({children,}:Readonly<{children: React.ReactNode;}>) {

    return (
      <html lang="en">
          <body>
            <Header />
              <main>
                  {children}
              </main>
            <Footer />
          </body>
      </html>
    )
}