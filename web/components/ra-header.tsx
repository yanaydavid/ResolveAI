"use client";

import Link from "next/link";
import Image from "next/image";
import { useLanguage } from "@/lib/lang-context";

export function RaHeader() {
  const { t, lang, setLang } = useLanguage();

  return (
    <header
      className="sticky top-0 z-50 border-b"
      style={{
        backgroundColor: "var(--ra-navy-950)",
        borderColor: "hsl(215 45% 18%)",
      }}
    >
      <div className="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between gap-6">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-3 shrink-0">
          <Image
            src="/logo.png"
            alt="ResolveAI"
            width={36}
            height={36}
            className="w-9 h-9 object-contain"
            onError={(e) => {
              (e.target as HTMLImageElement).src = "/logo.jpg";
            }}
          />
          <span
            className="text-xl font-display font-light tracking-wide hidden sm:block"
            style={{ color: "var(--ra-cream-50)" }}
          >
            ResolveAI
          </span>
        </Link>

        {/* Navigation */}
        <nav className="flex items-center gap-3">
          {/* Language Toggle */}
          <button
            onClick={() => setLang(lang === "he" ? "en" : "he")}
            className="text-xs tracking-widest uppercase px-3 py-1.5 border transition-colors cursor-pointer"
            style={{
              color: "var(--ra-gold-300)",
              borderColor: "hsl(42 48% 72% / 0.35)",
              fontFamily: "var(--font-sans)",
            }}
          >
            {t.nav.langToggle}
          </button>

          {/* New Case CTA */}
          <Link
            href="/new"
            className="text-xs tracking-widest uppercase px-5 py-2.5 font-medium transition-colors"
            style={{
              backgroundColor: "var(--ra-gold-500)",
              color: "var(--ra-navy-950)",
              fontFamily: "var(--font-sans)",
            }}
            onMouseEnter={(e) =>
              ((e.target as HTMLElement).style.backgroundColor =
                "var(--ra-gold-700)")
            }
            onMouseLeave={(e) =>
              ((e.target as HTMLElement).style.backgroundColor =
                "var(--ra-gold-500)")
            }
          >
            {t.nav.newCase}
          </Link>
        </nav>
      </div>
    </header>
  );
}
