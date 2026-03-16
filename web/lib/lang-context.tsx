"use client";

import {
  createContext,
  useContext,
  useState,
  useEffect,
  type ReactNode,
} from "react";

export type Lang = "he" | "en";

export const translations = {
  he: {
    nav: {
      newCase: "פתח תיק חדש",
      langToggle: "English",
      home: "ראשי",
    },
    hero: {
      eyebrow: "בוררות חכמה מבוססת בינה מלאכותית",
      title: "יישוב מחלוקות — מחדש.",
      subtitle:
        "במקום חודשים של הליכים משפטיים ועלויות גבוהות, קבלו פסיקה מבוססת בינה מלאכותית תוך ימים בודדים.",
      primaryCta: "פתח תיק חדש",
      secondaryCta: "כיצד זה עובד",
    },
    howItWorks: {
      label: "התהליך",
      title: "שלושה שלבים לפסיקה",
      steps: [
        {
          number: "01",
          title: "הגשת המחלוקת",
          desc: "תארו את הסכסוך, הגישו את טיעוניכם ושני הצדדים מעלים את המסמכים הרלוונטיים לבחינה.",
        },
        {
          number: "02",
          title: "ניתוח מעמיק",
          desc: "מערכת הבינה המלאכותית בוחנת בעומק את כלל הראיות, הטיעונים והמסמכים שהוגשו.",
        },
        {
          number: "03",
          title: "פסיקה מנומקת",
          desc: "קבלו פסיקה מפורטת ומנומקת הכוללת ניתוח הטיעונים, ממצאים וצעדי המשך מומלצים.",
        },
      ],
    },
    why: {
      label: "למה ResolveAI",
      title: "יתרון ברור על פני בית המשפט",
      benefits: [
        {
          title: "מהיר",
          desc: "פסיקה תוך ימים בודדים במקום חודשים של המתנה לדיון",
        },
        {
          title: "חסכוני",
          desc: "עלות שבריר בהשוואה לייצוג משפטי מסורתי ושכר טרחת עורך דין",
        },
        {
          title: "הוגן ואובייקטיבי",
          desc: "ניתוח נטול דעות קדומות, מבוסס ראיות ועקרונות משפטיים בלבד",
        },
        {
          title: "חסוי לחלוטין",
          desc: "כל המסמכים מוצפנים ומאובטחים ברמה הגבוהה ביותר",
        },
      ],
    },
    cta: {
      title: "מוכנים להתחיל?",
      subtitle:
        "הגישו את המחלוקת שלכם עוד היום וקבלו פסיקה מקצועית ומנומקת.",
      button: "פתח תיק חדש",
    },
    footer: {
      tagline: "בוררות חכמה מבוססת בינה מלאכותית",
      rights: "כל הזכויות שמורות",
    },
    form: {
      pageTitle: "פתיחת תיק חדש",
      pageSubtitle:
        "מלאו את הפרטים הבאים בקפידה. ככל שתפרטו יותר, כך הניתוח יהיה מדויק ומקיף יותר.",
      fields: {
        caseTitle: "כותרת המחלוקת",
        caseTitlePlaceholder: "תארו בקצרה את מהות הסכסוך",
        party1: "פרטי הצד המגיש",
        party2: "פרטי הצד שכנגד",
        name: "שם מלא",
        email: "כתובת דואר אלקטרוני",
        category: "קטגוריה",
        categoryPlaceholder: "בחרו קטגוריה",
        description: "תיאור המחלוקת",
        descriptionPlaceholder:
          "פרטו את הנסיבות, הטיעונים והסעד המבוקש. כללו תאריכים רלוונטיים, סכומים כספיים, והמסמכים המצורפים.",
        documents: "מסמכים רלוונטיים",
        documentsNote:
          "חוזים, כתבי תביעה, התכתבויות, קבלות — כל מסמך שיכול לתמוך בעמדתכם",
        documentsButton: "בחרו קבצים",
        documentsSelected: "קבצים נבחרו",
        submit: "הגש לבחינת AI",
        submitting: "הבינה המלאכותית מנתחת את התיק...",
      },
      categories: [
        { value: "business", label: "מסחרי ועסקי" },
        { value: "property", label: "נדל\"ן ורכוש" },
        { value: "financial", label: "פיננסי וכספי" },
        { value: "employment", label: "עבודה ותעסוקה" },
        { value: "contract", label: "הפרת חוזה" },
        { value: "other", label: "אחר" },
      ],
      errors: {
        required: "שדה חובה",
        invalidEmail: "כתובת דואר אלקטרוני לא תקינה",
        minLength: "יש להזין לפחות 30 תווים",
        apiError: "אירעה שגיאה בעיבוד הבקשה. אנא נסו שנית.",
      },
    },
    verdict: {
      title: "פסיקת הבוררות",
      caseLabel: "תיק מספר",
      date: "תאריך הפסיקה",
      sections: {
        summary: "תקציר המחלוקת",
        analysis: "ניתוח AI",
        finding: "פסיקה",
        rationale: "נימוקים",
        nextSteps: "צעדי המשך מומלצים",
      },
      newCase: "פתח תיק חדש",
      backHome: "חזרה לדף הבית",
      noData: "לא נמצאו נתוני תיק.",
      noDataSub: "ייתכן שפג תוקף הסשן. אנא הגישו את המחלוקת מחדש.",
      noDataAction: "חזרה להגשת מחלוקת",
      generatedBy:
        "פסיקה זו הופקה על ידי מערכת הבינה המלאכותית של ResolveAI ואינה מהווה ייעוץ משפטי",
    },
  },

  en: {
    nav: {
      newCase: "Open a New Case",
      langToggle: "עברית",
      home: "Home",
    },
    hero: {
      eyebrow: "AI-Powered Smart Arbitration",
      title: "Dispute Resolution — Reimagined.",
      subtitle:
        "Instead of months of litigation and mounting legal fees, receive a reasoned AI-powered arbitration decision within days.",
      primaryCta: "Open a New Case",
      secondaryCta: "How It Works",
    },
    howItWorks: {
      label: "The Process",
      title: "Three Steps to a Decision",
      steps: [
        {
          number: "01",
          title: "Submit Your Dispute",
          desc: "Describe the conflict, present your arguments, and both parties upload their relevant supporting documents.",
        },
        {
          number: "02",
          title: "In-Depth Analysis",
          desc: "Our AI system conducts a thorough examination of all submitted evidence, arguments, and documentation.",
        },
        {
          number: "03",
          title: "Reasoned Decision",
          desc: "Receive a detailed, reasoned arbitration decision including analysis of arguments, findings, and recommended next steps.",
        },
      ],
    },
    why: {
      label: "Why ResolveAI",
      title: "A Clear Advantage Over the Courtroom",
      benefits: [
        {
          title: "Swift",
          desc: "Decisions within days, not months of waiting for a hearing date",
        },
        {
          title: "Cost-Effective",
          desc: "A fraction of the cost of traditional legal representation and attorney fees",
        },
        {
          title: "Fair & Impartial",
          desc: "Evidence-based analysis, free from human bias and predisposition",
        },
        {
          title: "Fully Confidential",
          desc: "All documents encrypted and secured to the highest standards",
        },
      ],
    },
    cta: {
      title: "Ready to Get Started?",
      subtitle:
        "Submit your dispute today and receive a professional, reasoned arbitration decision.",
      button: "Open a New Case",
    },
    footer: {
      tagline: "AI-Powered Smart Arbitration",
      rights: "All rights reserved",
    },
    form: {
      pageTitle: "Open a New Case",
      pageSubtitle:
        "Complete the details below carefully. The more detail you provide, the more precise and comprehensive the analysis will be.",
      fields: {
        caseTitle: "Case Title",
        caseTitlePlaceholder: "Briefly describe the nature of the dispute",
        party1: "Your Details",
        party2: "Opposing Party",
        name: "Full Name",
        email: "Email Address",
        category: "Category",
        categoryPlaceholder: "Select a category",
        description: "Dispute Description",
        descriptionPlaceholder:
          "Detail the circumstances, arguments, and relief sought. Include relevant dates, monetary amounts, and references to attached documents.",
        documents: "Supporting Documents",
        documentsNote:
          "Contracts, pleadings, correspondence, receipts — any document that supports your position",
        documentsButton: "Choose Files",
        documentsSelected: "files selected",
        submit: "Submit for AI Review",
        submitting: "The AI is analyzing your case...",
      },
      categories: [
        { value: "business", label: "Commercial & Business" },
        { value: "property", label: "Real Estate & Property" },
        { value: "financial", label: "Financial & Monetary" },
        { value: "employment", label: "Employment & Labor" },
        { value: "contract", label: "Contract Breach" },
        { value: "other", label: "Other" },
      ],
      errors: {
        required: "This field is required",
        invalidEmail: "Please enter a valid email address",
        minLength: "Please enter at least 30 characters",
        apiError: "An error occurred while processing your request. Please try again.",
      },
    },
    verdict: {
      title: "Arbitration Decision",
      caseLabel: "Case No.",
      date: "Date of Decision",
      sections: {
        summary: "Dispute Summary",
        analysis: "AI Analysis",
        finding: "Finding",
        rationale: "Rationale",
        nextSteps: "Recommended Next Steps",
      },
      newCase: "Open a New Case",
      backHome: "Back to Home",
      noData: "No case data found.",
      noDataSub: "Your session may have expired. Please resubmit the dispute.",
      noDataAction: "Return to Dispute Submission",
      generatedBy:
        "This decision was generated by the ResolveAI artificial intelligence system and does not constitute legal advice",
    },
  },
};

// Shape type — both languages conform to this
export type TranslationShape = typeof translations["he"];

interface LangContextValue {
  lang: Lang;
  setLang: (lang: Lang) => void;
  t: TranslationShape;
  dir: "rtl" | "ltr";
}

const LangContext = createContext<LangContextValue | null>(null);

export function LangProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useState<Lang>("he");
  const dir = lang === "he" ? "rtl" : "ltr";

  useEffect(() => {
    document.documentElement.lang = lang;
    document.documentElement.dir = dir;
  }, [lang, dir]);

  return (
    <LangContext.Provider
      value={{ lang, setLang, t: translations[lang] as TranslationShape, dir }}
    >
      <div dir={dir} className="min-h-screen flex flex-col">
        {children}
      </div>
    </LangContext.Provider>
  );
}

export function useLanguage() {
  const ctx = useContext(LangContext);
  if (!ctx) throw new Error("useLanguage must be used within LangProvider");
  return ctx;
}
