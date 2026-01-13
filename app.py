import streamlit as st
import time
import os
from ai_engine import analyze_case, generate_arbitral_award_pdf, get_analysis_summary_html, generate_case_id
from database import save_case, get_case, create_user

# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Initialize session state
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'analysis_data' not in st.session_state:
    st.session_state.analysis_data = None
if 'case_id' not in st.session_state:
    st.session_state.case_id = None
if 'pdf_path' not in st.session_state:
    st.session_state.pdf_path = None
if 'portal_mode' not in st.session_state:
    st.session_state.portal_mode = 'claimant'
if 'defendant_registered' not in st.session_state:
    st.session_state.defendant_registered = False
if 'defendant_case_data' not in st.session_state:
    st.session_state.defendant_case_data = None

# Page configuration
st.set_page_config(
    page_title="Resolve AI - בוררות דיגיטלית",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS - Simple and clean design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');

    * {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
    }

    /* Hide Streamlit default elements */
    header[data-testid="stHeader"],
    footer {
        visibility: hidden;
        height: 0;
    }

    .block-container {
        padding-top: 0 !important;
        max-width: 100% !important;
    }

    /* Background */
    [data-testid="stAppViewContainer"] {
        background: #F1F5F9;
    }

    /* Custom Header - Sticky */
    .custom-header {
        background: #0A2647;
        height: 100px;
        position: sticky;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 5%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Logo */
    .logo {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo img {
        height: 60px;
        width: 60px;
        border-radius: 50%;
    }

    .logo-text {
        color: white;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .logo-ai {
        background: linear-gradient(135deg, #7C3AED, #6366F1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 80px 10% 60px;
        background: linear-gradient(135deg, #F1F5F9 0%, #E0E7FF 100%);
    }

    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #7C3AED, #6366F1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        letter-spacing: -2px;
    }

    .hero-subtitle {
        font-size: 1.8rem;
        color: #475569;
        font-weight: 500;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
        text-align: center;
    }

    /* Main Content */
    .main-content {
        padding: 60px 10%;
        max-width: 1400px;
        margin: 0 auto;
    }

    /* Card */
    .card {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        margin-bottom: 30px;
        transition: all 0.3s ease;
        color: #0A2647;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.12);
    }

    .card p {
        color: #0A2647;
    }

    /* Expander text color */
    .streamlit-expanderHeader {
        color: #0A2647 !important;
    }

    /* Checkbox text color */
    .stCheckbox label {
        color: #0A2647 !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #7C3AED, #6366F1) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px 40px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4) !important;
    }

    /* Text Inputs */
    .stTextInput input {
        border-radius: 10px !important;
        border: 2px solid #E2E8F0 !important;
        padding: 12px !important;
        font-size: 1.1rem !important;
        text-align: right !important;
        direction: rtl !important;
    }

    .stTextInput input:focus {
        border-color: #7C3AED !important;
    }

    /* File Uploader */
    .stFileUploader {
        border-radius: 10px !important;
    }

    /* RTL File Uploader - Browse button on right */
    [data-testid="stFileUploaderDropzone"] {{
        flex-direction: row-reverse !important;
        text-align: right !important;
    }}

    [data-testid="stFileUploaderDropzone"] section {{
        display: flex;
        flex-direction: row-reverse !important;
        align-items: center;
        gap: 15px;
    }}

    [data-testid="stFileUploaderDropzone"] button {{
        order: -1;
        margin-right: 0 !important;
        margin-left: auto !important;
    }}

    .stFileUploader label {{
        text-align: right !important;
        direction: rtl !important;
    }}

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .custom-header {
            height: auto;
            padding: 20px;
        }

        .hero-title {
            font-size: 3rem;
        }

        .hero-subtitle {
            font-size: 1.3rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="custom-header">
        <div class="logo">
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" alt="Resolve AI">
            <div class="logo-text">Resolve <span class="logo-ai">AI</span></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Resolve AI</h1>
        <p class="hero-subtitle">
            פתרון בוררות דיגיטלי מבוסס בינה מלאכותית -
            מהפכה בעולם יישוב סכסוכים משפטיים
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🔀 בחר פורטל")
    portal_choice = st.radio(
        "בחר את סוג המשתמש:",
        ["🏛️ פורטל תובעים", "🛡️ פורטל נתבעים"],
        key="portal_radio"
    )

    if portal_choice == "🏛️ פורטל תובעים":
        st.session_state.portal_mode = 'claimant'
    else:
        st.session_state.portal_mode = 'defendant'

    st.markdown("---")
    st.markdown("### 📞 צור קשר")
    st.markdown("support@resolveai.com")

# Main Content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# =========================
# CLAIMANT PORTAL
# =========================
if st.session_state.portal_mode == 'claimant':
    # Only show upload form if results are not displayed
    if not st.session_state.show_result:
        st.markdown("""
            <div class="card">
                <h2 style='color: #0A2647; font-size: 2.5rem; margin-bottom: 10px; text-align: center;'>
                    📋 הגשת תביעה
            </h2>
            <p style='font-size: 1.2rem; color: #64748B; text-align: center; margin-bottom: 30px;'>
                מלא את הפרטים להגשת כתב תביעה דיגיטלי
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Claimant Registration
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
            📝 פרטי התובע
        </h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        claimant_name = st.text_input(
            "שם מלא",
            key="claimant_name",
            placeholder="שם פרטי ושם משפחה",
            help="הכנס את שמך המלא (פרטי ומשפחה)"
        )

        claimant_email = st.text_input(
            "כתובת מייל",
            key="claimant_email",
            placeholder="example@email.com",
            help="הכנס את כתובת המייל שלך"
        )

    with col2:
        claimant_phone = st.text_input(
            "מספר טלפון נייד",
            key="claimant_phone",
            placeholder="05xxxxxxxx",
            help="הכנס את מספר הטלפון הנייד שלך"
        )

        claimant_file = st.file_uploader(
            "העלה כתב תביעה (PDF או Word)",
            type=["pdf", "docx"],
            key="claimant_file",
            help="העלה את כתב התביעה בפורמט PDF או Word (.docx)"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Defendant Information
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
            🛡️ פרטי הנתבע
        </h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        defendant_name = st.text_input(
            "שם מלא של הנתבע",
            key="defendant_name",
            placeholder="שם פרטי ושם משפחה",
            help="הכנס את השם המלא של הנתבע"
        )

    with col2:
        defendant_phone = st.text_input(
            "מספר טלפון נייד של הנתבע",
            key="defendant_phone",
            placeholder="05xxxxxxxx",
            help="הכנס את מספר הטלפון הנייד של הנתבע"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Terms of Service and Fees
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
        <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
            📜 תקנון ותנאי שימוש
        </h3>
    """, unsafe_allow_html=True)

    # Terms expander
    with st.expander("📖 לחץ לקריאת התקנון המלא"):
        st.markdown("""
        ### תקנון ותנאי שימוש - Resolve AI

        #### 1. כללי
        אתר Resolve AI (להלן: "השירות") הוא פלטפורמה טכנולוגית המשתמשת בבינה מלאכותית (AI) לצורך ניתוח מחלוקות, יצירת הצעות פשרה ומתן פסק בורר דיגיטלי.

        השימוש בשירות מותנה בהסכמת המשתמש לכל תנאי התקנון המפורטים להלן.

        השירות מיועד לשימושם של אנשים פרטיים ועסקים מעל גיל 18.

        #### 2. הצהרת אי-ייעוץ משפטי (Disclaimer)
        **השירות אינו מהווה ייעוץ משפטי:** המידע, הניתוחים ופסקי הדין המופקים על ידי המערכת מבוססים על אלגוריתמים של בינה מלאכותית.

        אין לראות בתוצרי המערכת תחליף לייעוץ עם עורך דין מוסמך.

        המפעיל אינו נושא באחריות לכל נזק שייגרם למשתמש כתוצאה מהסתמכות על פלט המערכת.

        #### 3. מודל הבוררות והסכמת הצדדים
        השימוש ב-Resolve AI לצורך פסק בורר מחייב הסכמה מפורשת בכתב של שני הצדדים למחלוקת.

        המשתמשים מצהירים כי ידוע להם שפסק הבורר מופק על ידי בינה מלאכותית, והם מוותרים על כל טענה כלפי המערכת בגין שיקול הדעת המופעל על ידי ה-AI.

        #### 4. אגרות ותשלומים
        השימוש בחלק משירותי האתר כרוך בתשלום אגרה:
        - **אגרת הגשת תביעה:** 120 ₪
        - **דמי משלוח דואר רשום:** 35 ₪ (יוחזרו לתובע במידה ויזכה)
        - **דמי בוררות סופיים:** 200 ₪ (לאחר קבלת פסק הדין)

        האגרות אינן ניתנות להחזר לאחר תחילת ניתוח התיק על ידי המערכת.

        החזר הוצאות משפט (כגון 35 ש"ח עבור מכתב רשום) ייקבע במסגרת פסק הדין הסופי לפי שיקול דעת המערכת.

        #### 5. פרטיות ואבטחת מידע
        העלאת מסמכים (PDF/Word) למערכת מהווה הסכמה לעיבודם על ידי מנועי בינה מלאכותית (כגון OpenAI/Anthropic).

        המערכת מתחייבת לא לעשות שימוש במידע האישי של המשתמשים למטרות פרסום ללא הסכמה.

        ידוע למשתמש כי המידע נשמר בענן וכי למרות אמצעי האבטחה, אין חסינות מוחלטת מפני פריצות.

        #### 6. הגבלת אחריות
        המפעיל לא יהיה אחראי לכל טעות בחישוב, בפרשנות החוק או בעובדות המוצגות על ידי ה-AI.

        האחריות המקסימלית של המפעיל כלפי המשתמש מוגבלת לגובה האגרה ששולמה עבור השירות בלבד.
        """)

    # Checkbox for terms acceptance
    terms_accepted = st.checkbox(
        "✅ אני מאשר/ת שקראתי והבנתי את התקנון ומסכים/ה לתנאי השימוש",
        key="terms_checkbox"
    )

    # Checkbox for postal mail
    postal_accepted = st.checkbox(
        "✅ אני מאשר/ת שליחת כתב התביעה דרך דואר רשום (עלות 35 ₪ - תיכלל בסכום התביעה במידה ואזכה)",
        key="postal_checkbox"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Submit button
    st.markdown('<br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 הגש תביעה", use_container_width=True):
            # Validation
            if not claimant_name or not claimant_phone or not claimant_email:
                st.error("⚠️ נא למלא את כל הפרטים האישיים של התובע")
            elif not defendant_name or not defendant_phone:
                st.error("⚠️ נא למלא את פרטי הנתבע (שם מלא וטלפון)")
            elif not claimant_file:
                st.error("⚠️ נא להעלות את כתב התביעה")
            elif not terms_accepted:
                st.error("⚠️ יש לאשר את התקנון ותנאי השימוש")
            elif not postal_accepted:
                st.error("⚠️ יש לאשר את שליחת הדואר הרשום")
            else:
                with st.status("📝 מעבד את כתב התביעה...", expanded=True) as status:
                    # Generate case ID
                    case_id = generate_case_id()

                    st.write("📄 שומר את כתב התביעה...")
                    time.sleep(0.5)

                    # Save uploaded file
                    claimant_file_path = os.path.join("uploads", f"{case_id}_{claimant_name}_claim.{claimant_file.name.split('.')[-1]}")

                    with open(claimant_file_path, "wb") as f:
                        f.write(claimant_file.getbuffer())

                    st.write("💾 רושם את התיק במערכת...")
                    time.sleep(0.5)

                    # Create user in database
                    create_user(claimant_name, claimant_phone, claimant_email, 'claimant')

                    # Save to database (without defendant file yet)
                    save_case(
                        case_id,
                        claimant_name,
                        claimant_phone,
                        claimant_email,
                        defendant_name,
                        defendant_phone,
                        claimant_file=claimant_file_path,
                        defendant_file=None,
                        pdf_path=None,
                        terms_accepted=True,
                        postal_mail_cost=35.0,
                        submission_fee=120.0
                    )

                    st.write("📧 שולח הודעות...")
                    time.sleep(0.5)

                    # Note: SMS and Email will be sent here once we have API keys
                    # For now, just show success message

                    # Save case ID for display
                    st.session_state.submitted_case_id = case_id
                    st.session_state.submitted_claimant_email = st.session_state.claimant_email
                    st.session_state.submitted_claimant_phone = st.session_state.claimant_phone
                    st.session_state.submitted_defendant_phone = st.session_state.defendant_phone

                    status.update(label="✅ התביעה נקלטה בהצלחה!", state="complete", expanded=False)

                st.session_state.show_result = True
                st.rerun()

# Display results - Case submitted successfully
if st.session_state.show_result and st.session_state.get('submitted_case_id'):
    # Display Case ID prominently
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                padding: 30px; border-radius: 20px; text-align: center; color: white; margin: 30px 0;
                box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);'>
        <h2 style='font-size: 2.5rem; margin-bottom: 20px;'>✅ התביעה הוגשה בהצלחה!</h2>
        <h3 style='font-size: 1.3rem; margin-bottom: 10px; opacity: 0.9;'>מספר תיק</h3>
        <h1 style='font-size: 3.5rem; font-weight: 900; margin: 0; letter-spacing: 3px;'>{st.session_state.submitted_case_id}</h1>
        <p style='margin-top: 15px; font-size: 1.1rem; opacity: 0.9;'>שמור מספר זה לעקוב אחרי התיק</p>
    </div>
    """, unsafe_allow_html=True)

    # Notification status
    st.markdown("""
        <div class="card">
            <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
                📬 הודעות נשלחו
            </h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="card">
                <h4 style='color: #10b981; text-align: center;'>📧 לתובע</h4>
                <p style='text-align: center; direction: rtl;'>
                    הודעה נשלחה למייל ול-SMS<br/>
                    עם מספר התיק וקישור למעקב
                </p>
            </div>
        """, unsafe_allow_html=True)
        if 'submitted_claimant_email' in st.session_state:
            st.info(f"📧 {st.session_state.submitted_claimant_email}")
        if 'submitted_claimant_phone' in st.session_state:
            st.info(f"📱 {st.session_state.submitted_claimant_phone}")

    with col2:
        st.markdown("""
            <div class="card">
                <h4 style='color: #f59e0b; text-align: center;'>📨 לנתבע</h4>
                <p style='text-align: center; direction: rtl;'>
                    SMS נשלח לנתבע<br/>
                    עם פרטי התביעה וקישור למערכת
                </p>
            </div>
        """, unsafe_allow_html=True)
        if 'submitted_defendant_phone' in st.session_state:
            st.info(f"📱 {st.session_state.submitted_defendant_phone}")

    # Next steps
    st.markdown("""
        <div class="card">
            <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
                📋 השלבים הבאים
            </h3>
            <div style='text-align: right; direction: rtl; line-height: 2; color: #0A2647;'>
                <p style='color: #0A2647;'><b>1️⃣ הנתבע יקבל הודעה</b> - SMS עם קישור לצפייה בתביעה</p>
                <p style='color: #0A2647;'><b>2️⃣ הנתבע ירשם למערכת</b> - יצטרך למלא פרטים אישיים</p>
                <p style='color: #0A2647;'><b>3️⃣ הנתבע יגיש כתב הגנה</b> - יעלה את התשובה שלו לתביעה</p>
                <p style='color: #0A2647;'><b>4️⃣ ניתוח AI</b> - המערכת תנתח את שני המסמכים</p>
                <p style='color: #0A2647;'><b>5️⃣ פסק בוררות</b> - תקבל החלטה מנומקת</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Show submitted case info if analysis exists
    if st.session_state.get('analysis_data'):
        st.markdown(get_analysis_summary_html(st.session_state.analysis_data), unsafe_allow_html=True)

    # PDF Download Button
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.session_state.pdf_path and os.path.exists(st.session_state.pdf_path):
            with open(st.session_state.pdf_path, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()

            st.download_button(
                label="📥 הורד פסק בוררות (PDF)",
                data=pdf_bytes,
                file_name=f"arbitral_award_{st.session_state.get('submitted_case_id', 'case')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

            st.success("""
                ✅ פסק הבוררות נוצר בהצלחה!

                המסמך כולל:
                - ניתוח מלא של כל נקודות המחלוקת
                - ההחלטה הסופית והנימוקים
                - סיכום כספי מפורט
                - אזור חתימות לשני הצדדים
            """)

    st.markdown('<br>', unsafe_allow_html=True)

    # Clear button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔙 חזור לדף הבית", use_container_width=True):
            st.session_state.show_result = False
            st.session_state.analysis_data = None
            st.session_state.submitted_case_id = None
            st.session_state.submitted_claimant_email = None
            st.session_state.submitted_claimant_phone = None
            st.session_state.submitted_defendant_phone = None
            st.session_state.pdf_path = None
            st.rerun()

# =========================
# DEFENDANT PORTAL
# =========================
elif st.session_state.portal_mode == 'defendant':
    st.markdown("""
        <div class="card">
            <h2 style='color: #0A2647; font-size: 2.5rem; margin-bottom: 10px; text-align: center;'>
                🛡️ פורטל נתבעים
            </h2>
            <p style='font-size: 1.2rem; color: #64748B; text-align: center; margin-bottom: 30px;'>
                הזן את מספר התיק שקיבלת ב-SMS
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Case ID lookup
    if not st.session_state.defendant_case_data:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
            <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
                🔍 חיפוש תיק
            </h3>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            case_id_input = st.text_input(
                "מספר תיק",
                key="case_id_lookup",
                placeholder="הכנס את מספר התיק שקיבלת ב-SMS",
                help="מספר תיק בן 10 ספרות"
            )

            if st.button("🔍 חפש תיק", use_container_width=True):
                if not case_id_input:
                    st.error("⚠️ נא להזין מספר תיק")
                else:
                    # Search for case
                    case = get_case(case_id_input)
                    if case:
                        st.session_state.defendant_case_data = case
                        st.success(f"✅ נמצא תיק מספר {case_id_input}")
                        st.rerun()
                    else:
                        st.error("❌ מספר תיק לא נמצא במערכת. אנא בדוק שהמספר נכון.")

        st.markdown('</div>', unsafe_allow_html=True)

    # Show case details and allow defendant to respond
    else:
        case = st.session_state.defendant_case_data

        # Check if defendant already registered
        if not st.session_state.defendant_registered:
            # Defendant registration
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f"""
                <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
                    📝 רישום נתבע
                </h3>
                <p style='text-align: center; direction: rtl; margin-bottom: 20px;'>
                    תיק מספר: <b>{case['case_id']}</b><br/>
                    נגדך הוגשה תביעה על ידי: <b>{case['claimant_name']}</b>
                </p>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                defendant_name = st.text_input(
                    "שם מלא",
                    key="defendant_reg_name",
                    placeholder="שם פרטי ושם משפחה",
                    value=case['defendant_name'],
                    help="הכנס את שמך המלא"
                )

                defendant_email = st.text_input(
                    "כתובת מייל",
                    key="defendant_reg_email",
                    placeholder="example@email.com",
                    help="הכנס את כתובת המייל שלך"
                )

            with col2:
                defendant_phone = st.text_input(
                    "מספר טלפון נייד",
                    key="defendant_reg_phone",
                    placeholder="05xxxxxxxx",
                    value=case['defendant_phone'],
                    help="הכנס את מספר הטלפון הנייד שלך"
                )

            st.markdown('<br>', unsafe_allow_html=True)

            if st.button("✅ אישור והמשך", use_container_width=True):
                if not defendant_name or not defendant_email or not defendant_phone:
                    st.error("⚠️ נא למלא את כל הפרטים")
                else:
                    # Register defendant
                    create_user(defendant_name, defendant_phone, defendant_email, 'defendant')
                    st.session_state.defendant_registered = True
                    st.success("✅ נרשמת בהצלחה!")
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

        else:
            # Show claim and allow defense upload
            st.markdown(f"""
                <div class="card">
                    <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
                        📄 כתב התביעה
                    </h3>
                    <p style='text-align: right; direction: rtl;'>
                        <b>תיק מספר:</b> {case['case_id']}<br/>
                        <b>תובע:</b> {case['claimant_name']}<br/>
                        <b>נתבע:</b> {case['defendant_name']}<br/>
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # Download claim file
            if case['claimant_file_path'] and os.path.exists(case['claimant_file_path']):
                with open(case['claimant_file_path'], "rb") as file:
                    st.download_button(
                        label="📥 הורד כתב תביעה",
                        data=file.read(),
                        file_name=f"claim_{case['case_id']}.{case['claimant_file_path'].split('.')[-1]}",
                        mime="application/pdf",
                        use_container_width=True
                    )

            st.markdown('<br>', unsafe_allow_html=True)

            # Defense upload
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("""
                <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px; text-align: center;'>
                    🛡️ הגשת כתב הגנה
                </h3>
            """, unsafe_allow_html=True)

            defense_file = st.file_uploader(
                "העלה כתב הגנה (PDF או Word)",
                type=["pdf", "docx"],
                key="defense_file",
                help="העלה את כתב ההגנה שלך בפורמט PDF או Word (.docx)"
            )

            if st.button("📤 הגש כתב הגנה", use_container_width=True):
                if not defense_file:
                    st.error("⚠️ נא להעלות כתב הגנה")
                else:
                    with st.status("📝 מעבד כתב הגנה...", expanded=True) as status:
                        st.write("📄 שומר את כתב ההגנה...")
                        time.sleep(0.5)

                        # Save defense file
                        defense_file_path = os.path.join("uploads", f"{case['case_id']}_{case['defendant_name']}_defense.{defense_file.name.split('.')[-1]}")
                        with open(defense_file_path, "wb") as f:
                            f.write(defense_file.getbuffer())

                        st.write("⚖️ מריץ ניתוח AI...")
                        time.sleep(1)

                        # Run AI analysis
                        analysis = analyze_case(case['claimant_name'], case['defendant_name'])

                        st.write("📄 יוצר פסק בוררות...")
                        time.sleep(1)

                        # Generate PDF
                        pdf_filename = f"arbitral_award_{case['case_id']}.pdf"
                        pdf_path = os.path.join("uploads", pdf_filename)

                        case_data = {
                            'case_id': case['case_id'],
                            'claimant': case['claimant_name'],
                            'defendant': case['defendant_name']
                        }

                        generate_arbitral_award_pdf(case_data, analysis, pdf_path)

                        # Update database with defense file and PDF
                        from database import init_database
                        init_database()
                        import sqlite3
                        conn = sqlite3.connect("resolve_ai.db")
                        cursor = conn.cursor()
                        cursor.execute("""
                            UPDATE cases
                            SET defendant_file_path = ?, pdf_path = ?, status = 'Completed'
                            WHERE case_id = ?
                        """, (defense_file_path, pdf_path, case['case_id']))
                        conn.commit()
                        conn.close()

                        st.session_state.analysis_data = analysis
                        st.session_state.case_id = case['case_id']
                        st.session_state.pdf_path = pdf_path
                        st.session_state.submitted_case_id = case['case_id']

                        status.update(label="✅ ניתוח הושלם!", state="complete", expanded=False)

                    st.success("✅ כתב ההגנה התקבל בהצלחה! מעבר לצפייה בפסק הבוררות...")
                    time.sleep(2)
                    st.session_state.show_result = True
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
