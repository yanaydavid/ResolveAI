import type { Metadata } from "next";
import {
  Cormorant_Garamond,
  Libre_Baskerville,
  Frank_Ruhl_Libre,
} from "next/font/google";
import { LangProvider } from "@/lib/lang-context";
import "./globals.css";

const cormorant = Cormorant_Garamond({
  subsets: ["latin"],
  weight: ["300", "400", "600", "700"],
  style: ["normal", "italic"],
  variable: "--font-cormorant",
  display: "swap",
});

const libreBaskerville = Libre_Baskerville({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-baskerville",
  display: "swap",
});

const frankRuhlLibre = Frank_Ruhl_Libre({
  subsets: ["hebrew", "latin"],
  weight: ["300", "400", "500", "700"],
  variable: "--font-frank-ruhl",
  display: "swap",
});

export const metadata: Metadata = {
  title: "ResolveAI — בוררות חכמה מבוססת בינה מלאכותית",
  description:
    "AI-powered dispute resolution. Fast, impartial arbitration decisions within days — without courts, lawyers, or waiting.",
  keywords: ["arbitration", "dispute resolution", "AI", "בוררות", "יישוב מחלוקות"],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="he"
      dir="rtl"
      className={`${cormorant.variable} ${libreBaskerville.variable} ${frankRuhlLibre.variable}`}
      suppressHydrationWarning
    >
      <body className="antialiased">
        <LangProvider>{children}</LangProvider>
      </body>
    </html>
  );
}
