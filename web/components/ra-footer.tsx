"use client";

import { useLanguage } from "@/lib/lang-context";

export function RaFooter() {
  const { t } = useLanguage();
  const year = new Date().getFullYear();

  return (
    <footer
      className="border-t py-10"
      style={{
        backgroundColor: "var(--ra-navy-950)",
        borderColor: "hsl(215 45% 18%)",
      }}
    >
      <div className="max-w-6xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex flex-col items-center sm:items-start gap-1">
          <span
            className="text-lg font-display font-light tracking-wider"
            style={{ color: "var(--ra-cream-50)" }}
          >
            ResolveAI
          </span>
          <span
            className="text-xs tracking-widest uppercase"
            style={{ color: "var(--ra-gold-300)", fontFamily: "var(--font-sans)" }}
          >
            {t.footer.tagline}
          </span>
        </div>

        <p
          className="text-xs"
          style={{
            color: "hsl(215 20% 45%)",
            fontFamily: "var(--font-sans)",
          }}
        >
          &copy; {year} ResolveAI. {t.footer.rights}.
        </p>
      </div>
    </footer>
  );
}
