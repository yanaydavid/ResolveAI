"use client";

import Link from "next/link";
import { RaHeader } from "@/components/ra-header";
import { RaFooter } from "@/components/ra-footer";
import { useLanguage } from "@/lib/lang-context";

export default function LandingPage() {
  const { t } = useLanguage();

  return (
    <>
      <RaHeader />

      <main className="flex-1">
        {/* ── Hero ──────────────────────────────────────────────── */}
        <section
          className="relative min-h-[92vh] flex items-center"
          style={{ backgroundColor: "var(--ra-navy-950)" }}
        >
          {/* Subtle ruled background */}
          <div
            className="absolute inset-0 opacity-[0.025] pointer-events-none"
            style={{
              backgroundImage:
                "repeating-linear-gradient(0deg, transparent, transparent 72px, hsl(42 48% 72%) 72px, hsl(42 48% 72%) 73px)",
            }}
            aria-hidden="true"
          />

          <div className="relative max-w-5xl mx-auto px-6 py-28 text-center w-full">
            <p
              className="text-xs tracking-[0.35em] uppercase mb-8"
              style={{
                color: "var(--ra-gold-300)",
                fontFamily: "var(--font-sans)",
              }}
            >
              {t.hero.eyebrow}
            </p>

            <span
              className="gold-rule block w-20 mx-auto mb-10"
              aria-hidden="true"
            />

            <h1
              className="text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-light italic leading-[1.08] mb-10"
              style={{
                color: "var(--ra-cream-50)",
                fontFamily: "var(--font-display)",
              }}
            >
              {t.hero.title}
            </h1>

            <p
              className="text-lg md:text-xl max-w-2xl mx-auto mb-14 leading-relaxed"
              style={{
                color: "hsl(40 28% 74%)",
                fontFamily: "var(--font-sans)",
              }}
            >
              {t.hero.subtitle}
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/new"
                className="inline-block px-10 py-4 text-xs tracking-[0.2em] uppercase font-semibold transition-colors"
                style={{
                  backgroundColor: "var(--ra-gold-500)",
                  color: "var(--ra-navy-950)",
                  fontFamily: "var(--font-sans)",
                }}
                onMouseEnter={(e) =>
                  ((e.currentTarget as HTMLElement).style.backgroundColor =
                    "var(--ra-gold-700)")
                }
                onMouseLeave={(e) =>
                  ((e.currentTarget as HTMLElement).style.backgroundColor =
                    "var(--ra-gold-500)")
                }
              >
                {t.hero.primaryCta}
              </Link>

              <a
                href="#how-it-works"
                className="inline-block px-10 py-4 text-xs tracking-[0.2em] uppercase border transition-all"
                style={{
                  borderColor: "hsl(42 48% 72% / 0.35)",
                  color: "var(--ra-gold-300)",
                  fontFamily: "var(--font-sans)",
                }}
                onMouseEnter={(e) => {
                  const el = e.currentTarget as HTMLElement;
                  el.style.borderColor = "var(--ra-gold-300)";
                  el.style.backgroundColor = "hsl(42 48% 72% / 0.07)";
                }}
                onMouseLeave={(e) => {
                  const el = e.currentTarget as HTMLElement;
                  el.style.borderColor = "hsl(42 48% 72% / 0.35)";
                  el.style.backgroundColor = "transparent";
                }}
              >
                {t.hero.secondaryCta}
              </a>
            </div>
          </div>
        </section>

        {/* ── How It Works ──────────────────────────────────────── */}
        <section
          id="how-it-works"
          className="py-28"
          style={{ backgroundColor: "var(--ra-cream-50)" }}
        >
          <div className="max-w-6xl mx-auto px-6">
            <div className="text-center mb-20">
              <p
                className="text-xs tracking-[0.3em] uppercase mb-4"
                style={{
                  color: "var(--ra-gold-500)",
                  fontFamily: "var(--font-sans)",
                }}
              >
                {t.howItWorks.label}
              </p>
              <h2
                className="text-3xl md:text-4xl lg:text-5xl font-light"
                style={{
                  color: "var(--ra-navy-900)",
                  fontFamily: "var(--font-display)",
                }}
              >
                {t.howItWorks.title}
              </h2>
              <span
                className="gold-rule block w-16 mx-auto mt-6"
                aria-hidden="true"
              />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-16 md:gap-10">
              {t.howItWorks.steps.map((step, i) => (
                <div
                  key={step.number}
                  className="flex flex-col items-center md:items-start text-center md:text-start"
                >
                  <p
                    className="text-8xl lg:text-9xl font-light leading-none mb-3 select-none"
                    style={{
                      color: "var(--ra-gold-100)",
                      fontFamily: "var(--font-display)",
                    }}
                    aria-hidden="true"
                  >
                    {step.number}
                  </p>

                  <span
                    className="gold-rule-start block w-12 mb-6"
                    aria-hidden="true"
                  />

                  <h3
                    className="text-xl md:text-2xl font-semibold mb-4"
                    style={{
                      color: "var(--ra-navy-900)",
                      fontFamily: "var(--font-display)",
                    }}
                  >
                    {step.title}
                  </h3>
                  <p
                    className="text-base leading-relaxed"
                    style={{
                      color: "hsl(215 20% 38%)",
                      fontFamily: "var(--font-sans)",
                    }}
                  >
                    {step.desc}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* ── Why ResolveAI ─────────────────────────────────────── */}
        <section
          className="py-28"
          style={{ backgroundColor: "var(--ra-navy-900)" }}
        >
          <div className="max-w-6xl mx-auto px-6">
            <div className="text-center mb-20">
              <p
                className="text-xs tracking-[0.3em] uppercase mb-4"
                style={{
                  color: "var(--ra-gold-300)",
                  fontFamily: "var(--font-sans)",
                }}
              >
                {t.why.label}
              </p>
              <h2
                className="text-3xl md:text-4xl lg:text-5xl font-light"
                style={{
                  color: "var(--ra-cream-50)",
                  fontFamily: "var(--font-display)",
                }}
              >
                {t.why.title}
              </h2>
              <span
                className="gold-rule block w-16 mx-auto mt-6"
                aria-hidden="true"
              />
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px"
              style={{ backgroundColor: "hsl(215 45% 17%)" }}
            >
              {t.why.benefits.map((benefit) => (
                <div
                  key={benefit.title}
                  className="p-8 lg:p-10"
                  style={{ backgroundColor: "hsl(215 45% 17%)" }}
                >
                  <div
                    className="w-8 h-px mb-6"
                    style={{ backgroundColor: "var(--ra-gold-500)" }}
                    aria-hidden="true"
                  />
                  <h3
                    className="text-xl font-semibold mb-4"
                    style={{
                      color: "var(--ra-gold-300)",
                      fontFamily: "var(--font-display)",
                    }}
                  >
                    {benefit.title}
                  </h3>
                  <p
                    className="text-sm leading-relaxed"
                    style={{
                      color: "hsl(40 20% 68%)",
                      fontFamily: "var(--font-sans)",
                    }}
                  >
                    {benefit.desc}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* ── CTA Banner ────────────────────────────────────────── */}
        <section
          className="py-28"
          style={{ backgroundColor: "var(--ra-navy-950)" }}
        >
          <div className="max-w-2xl mx-auto px-6 text-center">
            <span
              className="gold-rule block w-24 mx-auto mb-12"
              aria-hidden="true"
            />

            <h2
              className="text-3xl md:text-4xl lg:text-5xl font-light italic mb-8"
              style={{
                color: "var(--ra-cream-50)",
                fontFamily: "var(--font-display)",
              }}
            >
              {t.cta.title}
            </h2>

            <p
              className="text-base md:text-lg mb-14 leading-relaxed"
              style={{
                color: "hsl(40 28% 72%)",
                fontFamily: "var(--font-sans)",
              }}
            >
              {t.cta.subtitle}
            </p>

            <Link
              href="/new"
              className="inline-block px-14 py-5 text-xs tracking-[0.25em] uppercase font-semibold transition-colors"
              style={{
                backgroundColor: "var(--ra-gold-500)",
                color: "var(--ra-navy-950)",
                fontFamily: "var(--font-sans)",
              }}
              onMouseEnter={(e) =>
                ((e.currentTarget as HTMLElement).style.backgroundColor =
                  "var(--ra-gold-700)")
              }
              onMouseLeave={(e) =>
                ((e.currentTarget as HTMLElement).style.backgroundColor =
                  "var(--ra-gold-500)")
              }
            >
              {t.cta.button}
            </Link>
          </div>
        </section>
      </main>

      <RaFooter />
    </>
  );
}
