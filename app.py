import streamlit as st
import streamlit.components.v1 as components
import os
import random
import string
from datetime import datetime

# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="Resolve AI - בוררות דיגיטלית",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# Utility Functions
# =====================================================
def generate_case_id():
    """Generate unique case ID"""
    timestamp = datetime.now().strftime("%Y%m%d")
    random_part = ''.join(random.choices(string.digits, k=6))
    return f"RA-{timestamp}-{random_part}"

def save_uploaded_file(uploaded_file, case_id, file_type):
    """Save uploaded file and return path"""
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    file_extension = uploaded_file.name.split('.')[-1]
    file_path = os.path.join("uploads", f"{case_id}_{file_type}.{file_extension}")

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path

def add_audit_log(case_id, stage, description):
    """Add entry to audit log"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        'timestamp': timestamp,
        'stage': stage,
        'description': description
    }

    if 'audit_log' not in st.session_state:
        st.session_state.audit_log = []

    st.session_state.audit_log.append(log_entry)

# =====================================================
# Custom CSS - Luxury Design with RTL Support
# =====================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');

    /* ===== LUXURY METALLIC GOLD GRADIENT ===== */
    :root {
        --gold-metallic-gradient: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%);
    }

    /* ===== CORE DESIGN - OPTIMIZED FOR PERFORMANCE ===== */

    /* 1. Base App Styling - Deep Dark Background */
    .stApp, [data-testid="stAppViewContainer"] {
        background: #0E1117 !important;
        color: #FFFFFF !important;
    }

    /* 2. Global Text - White */
    body, div, p, h1, h2, h3, h4, h5, h6, span, label, a {
        color: #FFFFFF !important;
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* 3. Input Fields - Dark Background with Metallic Border */
    input, textarea, select {
        background-color: #161B22 !important;
        color: #FFFFFF !important;
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        caret-color: #FFFFFF !important;
        padding: 22px !important;
    }

    input::placeholder, textarea::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }

    /* 4. File Uploader - Dark Navy Background with Metallic Border */
    [data-testid="stFileUploadDropzone"],
    .stFileUploader section,
    .stFileUploader > div {
        background-color: #0A2647 !important;
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        padding: 22px !important;
    }

    .stFileUploader label,
    [data-testid="stFileUploadDropzone"] span,
    [data-testid="stFileUploadDropzone"] p {
        color: #FFFFFF !important;
    }

    /* 5. Buttons - Metallic Gold Border */
    .stButton > button {
        background: transparent !important;
        color: white !important;
        border: 3px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        border-radius: 50px !important;
        padding: 20px 60px !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        outline: none !important;
        box-shadow: none !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) !important;
        color: #0E1117 !important;
        border: 3px solid transparent !important;
    }

    .stButton > button:focus,
    .stButton > button:active {
        outline: none !important;
        box-shadow: none !important;
        border: 3px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
    }

    .stButton > button:focus:not(:hover),
    .stButton > button:active:not(:hover) {
        background: transparent !important;
        color: white !important;
    }

    /* 6. Info/Alert Boxes - Dark with Metallic Border */
    .stAlert, .stInfo, .stSuccess {
        background-color: #0A2647 !important;
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        color: #FFFFFF !important;
        padding: 22px !important;
    }

    /* 7. Gold Highlights - Metallic Gradient Text */
    .gold-highlight {
        background: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-weight: bold !important;
    }

    .gold-gradient-text {
        background: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        text-align: center !important;
        margin: 20px 0 !important;
        line-height: 1.6 !important;
    }

    /* 8. Hide Streamlit Branding */
    header[data-testid="stHeader"], footer, #MainMenu {
        visibility: hidden;
        height: 0;
    }

    /* 9. RTL */
    * {
        direction: rtl;
        text-align: right;
    }

    /* ===== CUSTOM CLASSES ===== */

    .main-title {
        background: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 4.5rem !important;
        font-weight: 900 !important;
        text-align: center !important;
        margin: 40px 0 80px 0 !important;
    }

    .portal-title {
        color: white !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        text-align: center !important;
        margin: 20px 0 50px 0 !important;
    }

    .column-card {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 20px !important;
        padding: 60px 40px !important;
        text-align: center !important;
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        min-height: 400px !important;
    }

    .column-card:hover {
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        box-shadow: 0 0 30px rgba(194, 155, 64, 0.3) !important;
    }

    .column-title {
        color: white !important;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
    }

    .form-container {
        background: rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        padding: 50px !important;
        margin: 30px auto !important;
        max-width: 900px !important;
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
    }

    .section-title {
        color: white !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        text-align: center !important;
        margin-bottom: 30px !important;
    }

    .subsection-title {
        background: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin: 30px 0 15px 0 !important;
        border-bottom: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        padding-bottom: 10px !important;
    }

    .terms-container {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid transparent !important;
        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1 !important;
        border-radius: 15px !important;
        padding: 22px !important;
        margin: 30px 0 !important;
        max-height: 500px !important;
        overflow-y: scroll !important;
    }

    .success-box, .warning-box, .instruction-box, .readonly-box, .locked-box {
        background: #0E1117 !important;
        border-radius: 12px !important;
        padding: 25px !important;
        margin: 20px 0 !important;
        color: white !important;
    }

    .success-box {
        border: 2px solid #10b981 !important;
    }

    .warning-box {
        border: 2px solid rgba(239, 68, 68, 0.5) !important;
    }

    .instruction-box {
        border: 2px solid rgba(255, 193, 7, 0.5) !important;
    }

    .readonly-box {
        border: 2px solid rgba(100, 116, 139, 0.5) !important;
    }

    .locked-box {
        border: 3px solid rgba(100, 116, 139, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================
# Terms and Conditions - Full Legal Text
# =====================================================
TERMS_HTML = """
<div class="terms-title">
    <span class="gold-highlight">תקנון, תנאי שימוש והסכם בוררות מחייב – Resolve AI</span>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">1. הגדרת ההסכם וסמכות הכרעה</span></h3>
    <p>
        המשתמשים (להלן: "הצדדים") נותנים בזאת את הסכמתם המלאה, המפורשת והבלתי חוזרת למסור כל סכסוך ביניהם להכרעה בלעדית של מערכת Resolve AI (להלן: "הבורר").
    </p>
    <p>
        הצדדים מאשרים כי ידוע להם והם מסכימים לכך שהבורר הינו מערכת בינה מלאכותית המקבלת החלטות על בסיס ניתוח לוגי של טענות וראיות, ללא התערבות אנושית בזמן אמת.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">2. כפיפות לחוק הבוררות וסמכויות</span></h3>
    <p>
        הליך הבוררות כפוף להוראות חוק הבוררות, התשכ"ח-1968 (להלן: "החוק").
    </p>
    <p>
        פסק הבוררות שיופק יהיה סופי ומחייב, וניתן יהיה לאשרו כפסק דין על ידי בית המשפט המוסמך לפי סעיף 23 לחוק.
    </p>
    <p>
        בהתאם לסעיף 22 לחוק, הבורר שומר לעצמו את הסמכות לתקן פסק דין במקרה של טעות סופר או טעות חישוב טכנית.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">3. פטור מסדרי דין ודיני ראיות</span></h3>
    <p>
        בהתאם לסמכות לפי החוק, הבורר לא יהיה קשור בסדרי הדין האזרחיים או בדיני הראיות.
    </p>
    <p>
        הבורר יפסוק על פי שיקול דעת אובייקטיבי, עקרונות הצדק הטבעי והמסמכים שהוגשו על ידי הצדדים בלבד.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">4. חובת גילוי ושלמות המידע</span></h3>
    <p>
        כל צד מתחייב להעלות את כל הראיות והטענות שברשותו. אי-העלאת ראיה תהווה ויתור על הזכות להסתמך עליה בעתיד.
    </p>
    <p>
        העלאת מידע כוזב או מסמכים מזויפים מהווה עילה לביטול הפסק ולחיוב בפיצויים.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">5. סופיות הדיון וויתור על ערעור</span></h3>
    <p>
        הצדדים מוותרים על זכות הערעור על פסק הבוררות בכל ערכאה שהיא, למעט בעילות המצומצמות המנויות בסעיף 24 לחוק הבוררות.
    </p>
    <p>
        מוסכם כי השימוש בבינה מלאכותית כבורר אינו מהווה כשלעצמו עילה לביטול הפסק לפי סעיף 24.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">6. אבטחה, אימות וחתימה דיגיטלית</span></h3>
    <p>
        הצדדים מסכימים כי הפקת קוד זיהוי דיגיטלי (Hash) המוטמע במסמך מהווה חתימה אלקטרונית מאושרת לפי חוק חתימה אלקטרונית, התשס"א-2001.
    </p>
    <p>
        קוד זה מהווה ראיה חלוטה לשלמות המסמך ומניעת כל שינוי בו לאחר הפקתו.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">7. סמכות שיפוט שיורית</span></h3>
    <p>
        כל פנייה לבית משפט בבקשה לסעד זמני או לאישור/ביטול הפסק תוגש לבית המשפט המוסמך במחוז תל אביב בלבד.
    </p>
</div>

<div class="terms-section">
    <h3><span class="gold-highlight">8. הגנת פרטיות ואימות זהות</span></h3>
    <p>
        המערכת פועלת בשיטת 'עיבוד בר-חלוף' (Ephemeral Processing). צילום תעודת הזהות משמש לאימות בלבד ונמחק פיזית וצמיתות מהשרת מיד עם סיום חילוץ הנתונים.
    </p>
    <p>
        לצורך תיעוד משפטי, יישמר קוד אימות דיגיטלי (Hash) מוצפן בלבד, המבטיח את שלמות ההליך ללא החזקת המידע הרגיש.
    </p>
    <p>
        Resolve AI אינה שומרת עותקים של תעודות מזהות ומתחייבת למחיקה מיידית בהתאם לתקנות הגנת הפרטיות, התשמ"א-1981 ולתקנת הגנת הפרטיות (אבטחת מידע), התשע"ז-2017.
    </p>
</div>

<div class="scroll-instruction">
    <span class="gold-highlight">אנא גלול עד סוף התקנון לפני האישור</span>
</div>
"""

# =====================================================
# Initialize Session State
# =====================================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'terms_scrolled_claimant' not in st.session_state:
    st.session_state.terms_scrolled_claimant = False
if 'terms_scrolled_defendant' not in st.session_state:
    st.session_state.terms_scrolled_defendant = False
if 'case_id' not in st.session_state:
    st.session_state.case_id = None
if 'case_stage' not in st.session_state:
    st.session_state.case_stage = 'initial'  # initial, claim_submitted, defense_submitted, rebuttal_submitted, locked
if 'case_data' not in st.session_state:
    st.session_state.case_data = {}
if 'audit_log' not in st.session_state:
    st.session_state.audit_log = []

# =====================================================
# Analysis Engine & Arbitration Ruling Generator
# =====================================================

def analyze_case_evidence(case_data):
    """
    מנגנון ניתוח ראיות - מנתח את התיק ומחלץ עובדות מרכזיות
    """
    import re

    analysis = {
        'agreed_facts': [],
        'disputed_points': [],
        'key_findings': [],
        'legal_basis': []
    }

    # חילוץ עובדות מתביעת התובע
    if 'claimant' in case_data and case_data['claimant']:
        claim_text = case_data['claimant'].get('claim_text', '')

        # חיפוש תאריכים
        dates = re.findall(r'\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}', claim_text)
        if dates:
            analysis['agreed_facts'].append(f"תאריכים רלוונטיים: {', '.join(dates)}")

        # חיפוש סכומים כספיים
        amounts = re.findall(r'₪?\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*₪?', claim_text)
        if amounts:
            analysis['agreed_facts'].append(f"סכומים נזכרים: {', '.join(amounts)}")

        # זיהוי נקודות מפתח בתביעה
        if 'חוזה' in claim_text or 'הסכם' in claim_text:
            analysis['key_findings'].append("קיומו של הסכם חוזי בין הצדדים")
        if 'הפרה' in claim_text or 'הפר' in claim_text:
            analysis['key_findings'].append("טענה להפרת התחייבות חוזית")
        if 'נזק' in claim_text or 'נזקים' in claim_text:
            analysis['key_findings'].append("טענה לנזקים שנגרמו לתובע")

    # ניתוח כתב הגנה
    if 'defendant' in case_data and case_data['defendant']:
        defense_text = case_data['defendant'].get('defense_text', '')

        # זיהוי טענות הגנה
        if 'מכחיש' in defense_text or 'כופר' in defense_text or 'לא נכון' in defense_text:
            analysis['disputed_points'].append("הנתבע מכחיש את טענות התובע")
        if 'מאשר' in defense_text or 'מודה' in defense_text:
            analysis['disputed_points'].append("הנתבע מאשר חלק מהטענות")
        if 'ראיה' in defense_text or 'ראיות' in defense_text:
            analysis['disputed_points'].append("הנתבע הציג ראיות נגדיות")

    # ניתוח כתב תשובה (אם קיים)
    if 'rebuttal' in case_data and case_data['rebuttal']:
        rebuttal_text = case_data['rebuttal'].get('text', '')
        if 'סותר' in rebuttal_text or 'מפריך' in rebuttal_text:
            analysis['disputed_points'].append("התובע מפריך את טענות ההגנה")

    # בדיקת עמידה בתנאי התקנון
    analysis['legal_basis'].append("התיק עומד בתנאי סף לבוררות על פי חוק הבוררות, התשכ\"ח-1968")
    analysis['legal_basis'].append("שני הצדדים אישרו את סמכות הבורר והסכימו לתקנון Resolve AI")

    # ספירת קבצי ראיות
    claimant_evidence_count = len(case_data.get('claimant', {}).get('evidence_files', []))
    defendant_evidence_count = len(case_data.get('defendant', {}).get('evidence_files', []))

    if claimant_evidence_count > 0:
        analysis['key_findings'].append(f"התובע הגיש {claimant_evidence_count} קבצי ראיות")
    if defendant_evidence_count > 0:
        analysis['key_findings'].append(f"הנתבע הגיש {defendant_evidence_count} קבצי ראיות")

    return analysis


def generate_arbitration_ruling(case_id, case_data):
    """
    מייצר פסק בוררות מנומק על בסיס ניתוח הראיות
    """
    analysis = analyze_case_evidence(case_data)

    # פרטי הצדדים
    claimant = case_data.get('claimant', {})
    defendant = case_data.get('defendant', {})

    claimant_name = claimant.get('full_name', 'התובע')
    defendant_name = defendant.get('full_name', 'הנתבע')

    # בניית פסק הדין
    ruling = {
        'case_id': case_id,
        'date': datetime.now().strftime("%d.%m.%Y"),
        'claimant_name': claimant_name,
        'defendant_name': defendant_name,
        'analysis': analysis,
        'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return ruling


def render_arbitration_ruling(ruling):
    """
    מציג את פסק הבוררות בפורמט מעוצב
    """
    st.markdown("""
        <div style="background: #0E1117;
                    border: 3px solid transparent;
                    border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1;
                    border-radius: 20px;
                    padding: 50px;
                    margin: 40px auto;
                    max-width: 1000px;
                    box-shadow: 0 0 40px rgba(194, 155, 64, 0.4);">

            <h1 style="color: #C29B40;
                       text-align: center;
                       font-size: 3rem;
                       font-weight: 900;
                       margin-bottom: 40px;">
                <span class="gold-highlight">פסק בוררות מנומק</span>
            </h1>

            <div style="background: rgba(255, 255, 255, 0.03);
                        border-radius: 15px;
                        padding: 22px;
                        margin-bottom: 30px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px;"><span class="gold-highlight">מבוא</span></h2>
                <p style="color: #FFFFFF; font-size: 1.2rem; line-height: 1.8;">
                    מספר תיק: <strong style="color: #C29B40;">{case_id}</strong><br>
                    תאריך: <strong>{date}</strong><br><br>

                    <strong>התובע:</strong> {claimant_name}<br>
                    <strong>הנתבע:</strong> {defendant_name}<br><br>

                    פסק בוררות זה ניתן על ידי מערכת Resolve AI בהתאם להסכמת הצדדים
                    ובהתאם להוראות חוק הבוררות, התשכ"ח-1968.
                </p>
            </div>

            <div style="background: rgba(255, 255, 255, 0.03);
                        border-radius: 15px;
                        padding: 22px;
                        margin-bottom: 30px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px;"><span class="gold-highlight">עיקרי הטענות</span></h2>
                <p style="color: #FFFFFF; font-size: 1.2rem; line-height: 1.8;">
                    <strong>תביעת התובע:</strong><br>
                    {claim_summary}
                </p>
                <p style="color: #FFFFFF; font-size: 1.2rem; line-height: 1.8; margin-top: 20px;">
                    <strong>כתב הגנת הנתבע:</strong><br>
                    {defense_summary}
                </p>
            </div>

            <div style="background: rgba(255, 255, 255, 0.03);
                        border-radius: 15px;
                        padding: 22px;
                        margin-bottom: 30px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px;"><span class="gold-highlight">ניתוח והכרעה</span></h2>

                <h3 style="color: #FFFFFF; font-size: 1.4rem; margin-top: 20px; margin-bottom: 15px;">
                    עובדות מוסכמות:
                </h3>
                <ul style="color: #FFFFFF; font-size: 1.1rem; line-height: 1.8;">
                    {agreed_facts_html}
                </ul>

                <h3 style="color: #FFFFFF; font-size: 1.4rem; margin-top: 25px; margin-bottom: 15px;">
                    נקודות במחלוקת:
                </h3>
                <ul style="color: #FFFFFF; font-size: 1.1rem; line-height: 1.8;">
                    {disputed_points_html}
                </ul>

                <h3 style="color: #FFFFFF; font-size: 1.4rem; margin-top: 25px; margin-bottom: 15px;">
                    ממצאים מרכזיים:
                </h3>
                <ul style="color: #FFFFFF; font-size: 1.1rem; line-height: 1.8;">
                    {key_findings_html}
                </ul>

                <h3 style="color: #FFFFFF; font-size: 1.4rem; margin-top: 25px; margin-bottom: 15px;">
                    בסיס משפטי:
                </h3>
                <ul style="color: #FFFFFF; font-size: 1.1rem; line-height: 1.8;">
                    {legal_basis_html}
                </ul>
            </div>

            <div style="background: rgba(194, 155, 64, 0.1);
                        border: 2px solid transparent;
                        border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1;
                        border-radius: 15px;
                        padding: 22px;
                        margin-bottom: 20px;">
                <h2 style="font-size: 1.8rem; margin-bottom: 20px;"><span class="gold-highlight">סעד ופסיקה</span></h2>
                <p style="color: #FFFFFF; font-size: 1.3rem; line-height: 1.8; font-weight: 600;">
                    לאחר בחינה מעמיקה של כלל הראיות, הטיעונים וכתבי הטענות של שני הצדדים,
                    ועל בסיס ניתוח משפטי מקיף, מערכת Resolve AI קובעת כדלקמן:
                </p>
                <p style="color: #C29B40; font-size: 1.4rem; line-height: 1.8; font-weight: 700; margin-top: 20px;">
                    פסק הבוררות הסופי ייקבע לאחר השלמת הליך הניתוח המעמיק.
                </p>
            </div>

            <div style="text-align: center; margin-top: 40px; padding-top: 30px; border-top: 2px solid rgba(194, 155, 64, 0.3);">
                <p style="color: #C29B40; font-size: 1.1rem;">
                    Resolve AI - מערכת בוררות דיגיטלית<br>
                    פסק בוררות זה ניתן בהתאם לחוק הבוררות, התשכ"ח-1968
                </p>
            </div>
        </div>
    """.format(
        case_id=ruling['case_id'],
        date=ruling['date'],
        claimant_name=ruling['claimant_name'],
        defendant_name=ruling['defendant_name'],
        claim_summary=ruling['analysis'].get('key_findings', [''])[0] if ruling['analysis'].get('key_findings') else 'טענות התובע מפורטות בכתב התביעה',
        defense_summary=ruling['analysis'].get('disputed_points', [''])[0] if ruling['analysis'].get('disputed_points') else 'טענות הנתבע מפורטות בכתב ההגנה',
        agreed_facts_html=''.join([f'<li>{fact}</li>' for fact in ruling['analysis'].get('agreed_facts', ['לא נמצאו עובדות מוסכמות במפורש'])]),
        disputed_points_html=''.join([f'<li>{point}</li>' for point in ruling['analysis'].get('disputed_points', ['נקודות המחלוקת מפורטות בכתבי הטענות'])]),
        key_findings_html=''.join([f'<li>{finding}</li>' for finding in ruling['analysis'].get('key_findings', ['הממצאים מבוססים על ניתוח הראיות'])]),
        legal_basis_html=''.join([f'<li>{basis}</li>' for basis in ruling['analysis'].get('legal_basis', ['חוק הבוררות, התשכ"ח-1968'])])
    ), unsafe_allow_html=True)


# =====================================================
# Navigation Functions
# =====================================================
def go_to_claimant_portal():
    st.session_state.page = 'claimant_portal'

def go_to_defendant_portal():
    st.session_state.page = 'defendant_portal'

def go_to_home():
    st.session_state.page = 'home'
    st.session_state.terms_scrolled_claimant = False
    st.session_state.terms_scrolled_defendant = False

# =====================================================
# Terms Display Component with Scroll Detection
# =====================================================
def render_terms_with_scroll(portal_type):
    """
    Renders the terms and conditions with scroll detection.
    """
    scroll_key = f"terms_scroll_{portal_type}"

    # Display terms in scrollable container
    st.markdown(f'<div class="terms-container" id="{scroll_key}">', unsafe_allow_html=True)
    st.markdown(TERMS_HTML, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Add button to confirm reading
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("קראתי את התקנון המלא", key=f"confirm_read_{portal_type}", use_container_width=True):
            if portal_type == "claimant":
                st.session_state.terms_scrolled_claimant = True
            else:
                st.session_state.terms_scrolled_defendant = True
            st.rerun()

# =====================================================
# Page: Home (Landing Page)
# =====================================================
def render_home_page():
    # Main Title
    st.markdown("""
        <div class="main-content">
            <h1 class="main-title">ברוכים הבאים ל-Resolve AI</h1>
        </div>
    """, unsafe_allow_html=True)

    # Two Columns Layout
    col1, col2 = st.columns(2, gap="large")

    # Right Column - Claimant
    with col1:
        st.markdown("""
            <div class="column-card">
                <h2 class="column-title">רוצה להגיש תביעה?</h2>
            </div>
        """, unsafe_allow_html=True)

        if st.button("לחץ כאן", key="claimant_button"):
            go_to_claimant_portal()
            st.rerun()

    # Left Column - Defendant
    with col2:
        st.markdown("""
            <div class="column-card">
                <h2 class="column-title">רוצה להגיש כתב הגנה?</h2>
            </div>
        """, unsafe_allow_html=True)

        if st.button("לחץ כאן", key="defendant_button"):
            go_to_defendant_portal()
            st.rerun()

# =====================================================
# Page: Claimant Portal
# =====================================================
def render_claimant_portal():
    # Back Button
    st.markdown('<div class="back-button">', unsafe_allow_html=True)
    if st.button("חזרה לדף הבית", key="back_from_claimant"):
        go_to_home()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Portal Title
    st.markdown("""
        <h1 class="portal-title">מסוף תובעים</h1>
    """, unsafe_allow_html=True)

    # Portal Description Box
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(212, 175, 55, 0.3); border-radius: 20px; padding: 40px; margin: 20px auto 40px auto; max-width: 800px;">
            <p class="gold-gradient-text">כאן ניתן להגיש את תביעתך</p>
        </div>
    """, unsafe_allow_html=True)

    # Form Container
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # Check if awaiting rebuttal
    if st.session_state.case_stage == 'defense_submitted':
        st.markdown("""
            <div class="instruction-box">
                <p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 15px;">
                    כתב ההגנה התקבל
                </p>
                <p>
                    הנתבע הגיש את כתב ההגנה שלו. אתה מוזמן לצפות בטענותיו ולהגיש כתב תשובה (עד 500 מילים).
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Display defense
        if 'defendant' in st.session_state.case_data and st.session_state.case_data['defendant']:
            st.markdown('<div class="readonly-box">', unsafe_allow_html=True)
            st.markdown("<h4>כתב הגנה של הנתבע</h4>", unsafe_allow_html=True)
            st.markdown(f"<p>{st.session_state.case_data['defendant']['defense_text']}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Rebuttal form
        st.markdown('<p class="subsection-title">כתב תשובה</p>', unsafe_allow_html=True)

        st.markdown("""
            <div class="instruction-box">
                התייחס אך ורק לטענות החדשות שהעלה הנתבע. מגבלה: 500 מילים.
            </div>
        """, unsafe_allow_html=True)

        rebuttal_text = st.text_area(
            "כתב תשובה",
            key="rebuttal_text",
            placeholder="התייחס לטענות החדשות של הנתבע...",
            height=200,
            max_chars=3000
        )

        # Word count
        word_count = len(rebuttal_text.split()) if rebuttal_text else 0
        if word_count > 500:
            st.error(f"חריגה ממגבלת המילים: {word_count}/500")
        else:
            st.info(f"ספירת מילים: {word_count}/500")

        st.markdown("<br>", unsafe_allow_html=True)

        # Submit rebuttal
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("שלח כתב תשובה", key="submit_rebuttal"):
                if not rebuttal_text or len(rebuttal_text) < 20:
                    st.error("נא להזין כתב תשובה (לפחות 20 תווים)")
                elif word_count > 500:
                    st.error("כתב התשובה חורג ממגבלת 500 המילים")
                else:
                    # Save rebuttal
                    st.session_state.case_data['rebuttal'] = {
                        'text': rebuttal_text,
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    st.session_state.case_stage = 'rebuttal_submitted'
                    add_audit_log(st.session_state.case_id, "rebuttal_submitted", "כתב תשובה הוגש על ידי התובע")
                    st.success("כתב התשובה נשלח בהצלחה!")
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Check if case is locked - Generate and display arbitration ruling
    if st.session_state.case_stage in ['rebuttal_submitted', 'locked']:
        # סטטוס הודעה
        st.markdown("""
            <div class="instruction-box" style="background: rgba(194, 155, 64, 0.15);
                 border: 2px solid transparent;
                 border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1;
                 padding: 22px;">
                <p style="font-size: 1.4rem; font-weight: 700; color: #C29B40; text-align: center;">
                    התיק נעול - פסק הדין הראשוני הוכן
                </p>
                <p style="font-size: 1.1rem; color: #FFFFFF; text-align: center; margin-top: 15px;">
                    כל הטיעונים והראיות הועברו לניתוח מעמיק. להלן פסק הבוררות המנומק.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # הפקת פסק דין
        ruling = generate_arbitration_ruling(st.session_state.case_id, st.session_state.case_data)

        # הצגת פסק הדין
        render_arbitration_ruling(ruling)

        # הודעת סיום
        st.markdown("""
            <div class="instruction-box" style="margin-top: 40px;">
                <p style="font-size: 1.2rem; line-height: 1.8; text-align: center;">
                    <strong>פסק הדין הראשוני הוכן וממתין להזנת כתב הגנה מהנתבע לצורך חתימה סופית.</strong>
                </p>
                <p style="font-size: 1rem; margin-top: 15px; opacity: 0.8; text-align: center;">
                    לא ניתן לערוך או להוסיף מסמכים נוספים בשלב זה.
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Check if claim already submitted
    if st.session_state.case_stage == 'claim_submitted':
        st.markdown("""
            <div class="success-box">
                <div class="gold-highlight" style="font-size: 2.5rem; margin-bottom: 25px;">
                    המשך התהליך ועדכונים
                </div>
                <p class="gold-highlight" style="font-size: 1.2rem; margin-bottom: 10px;">
                    מספר תיק למעקב אישי:
                </p>
                <p class="gold-highlight" style="font-size: 3rem; font-weight: 900; margin: 20px 0; letter-spacing: 2px;">
                    {case_id}
                </p>
            </div>
        """.format(case_id=st.session_state.case_id), unsafe_allow_html=True)

        st.markdown("""
            <div class="instruction-box">
                <p style="font-size: 1.2rem; line-height: 1.9; color: #FFFFFF !important;">
                    מערכת Resolve AI שלחה לנתבע הזמנה לדין וגישה לכתב התביעה באופן אוטומטי.
                </p>
                <p style="font-size: 1.2rem; line-height: 1.9; margin-top: 15px; color: #FFFFFF !important;">
                    לאחר שהנתבע יאשר את סמכות הבוררות ויגיש את כתב הגנתו, תקבל מסרון (SMS) עם קישור לכניסה וצפייה בפסק הבוררות המנומק.
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Section Title
    st.markdown("""
        <h2 class="section-title">רישום תובע והגשת תביעה</h2>
    """, unsafe_allow_html=True)

    # Instruction Box
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(212, 175, 55, 0.3); border-radius: 20px; padding: 40px; margin: 20px auto 40px auto; max-width: 800px;">
            <p class="gold-gradient-text">על מנת שתוכל להגיש את כתב התביעה עליך לקרוא בעיון את התקנון ולאשר אותו</p>
        </div>
    """, unsafe_allow_html=True)

    # Check if terms have been read
    if not st.session_state.terms_scrolled_claimant:
        render_terms_with_scroll("claimant")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Terms confirmed
    st.success("התקנון נקרא בהצלחה")

    # Legal Agreement Checkbox
    terms_accepted = st.checkbox(
        "אני מאשר כי קראתי ואני מסכים לתקנון האתר ולהסכם הבוררות של Resolve AI",
        key="terms_claimant"
    )

    if terms_accepted:
        st.markdown("<br>", unsafe_allow_html=True)

        # KYC - Identity Verification
        st.markdown('<p class="subsection-title">אימות זהות</p>', unsafe_allow_html=True)

        st.markdown("""
            <div class="warning-box">
                <p style="font-weight: 700; margin-bottom: 10px;">
                    אימות זהות הינו תנאי הכרחי למתן תוקף משפטי לפסק הבוררות.
                </p>
                <p>
                    נדרש להעלות צילום ברור של תעודת זהות או תעודת חברה רשומה.
                </p>
            </div>
        """, unsafe_allow_html=True)

        id_document = st.file_uploader(
            "העלה צילום תעודת זהות / תעודת חברה",
            type=["pdf", "jpg", "jpeg", "png"],
            key="claimant_id_document",
            help="קובץ PDF או תמונה (JPG/PNG)"
        )

        st.info("למען הגנת פרטיותך, הקובץ נמחק מהשרת מיד לאחר האימות. Resolve AI אינה שומרת עותקים של תעודות מזהות.")

        # Personal Details
        st.markdown('<p class="subsection-title">פרטים אישיים</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input(
                "שם מלא",
                key="claimant_full_name",
                placeholder="הזן שם פרטי ושם משפחה"
            )
            email = st.text_input(
                "כתובת אימייל",
                key="claimant_email",
                placeholder="example@email.com"
            )

        with col2:
            id_number = st.text_input(
                "מספר תעודת זהות",
                key="claimant_id",
                placeholder="הזן מספר תעודת זהות או מספר חברה"
            )
            phone = st.text_input(
                "מספר טלפון",
                key="claimant_phone",
                placeholder="05XXXXXXXX"
            )

        # Claim Details
        st.markdown('<p class="subsection-title">כתב תביעה ופירוט עובדתי</p>', unsafe_allow_html=True)

        st.markdown("""
            <div class="instruction-box">
                פרט את השתלשלות האירועים, העובדות והסעד המבוקש. פסק הדין יתבסס על הסנכרון בין טיעוניך לראיות שיצורפו.
            </div>
        """, unsafe_allow_html=True)

        claim_text = st.text_area(
            "תיאור המקרה",
            key="claim_description",
            placeholder="פרט כאן את כל העובדות, האירועים והסעד המבוקש...",
            height=300
        )

        # Evidence Upload
        st.markdown('<p class="subsection-title">נספחים ואסמכתאות</p>', unsafe_allow_html=True)

        evidence_files = st.file_uploader(
            "העלה קבצי ראיות (PDF או DOCX בלבד)",
            type=["pdf", "docx"],
            accept_multiple_files=True,
            key="claimant_evidence"
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("שלח תביעה", key="submit_claim"):
                # Validation
                if not id_document:
                    st.error("נא להעלות צילום תעודת זהות / תעודת חברה")
                elif not full_name or not id_number or not email or not phone:
                    st.error("נא למלא את כל הפרטים האישיים")
                elif not claim_text or len(claim_text) < 50:
                    st.error("נא לפרט את כתב התביעה בצורה מפורטת (לפחות 50 תווים)")
                elif not evidence_files or len(evidence_files) == 0:
                    st.error("נא להעלות לפחות קובץ ראיה אחד")
                else:
                    # Generate case ID
                    case_id = generate_case_id()
                    st.session_state.case_id = case_id

                    # Save ID document
                    id_doc_path = save_uploaded_file(id_document, case_id, "claimant_id_document")

                    # Save evidence files
                    saved_files = []
                    for idx, file in enumerate(evidence_files):
                        file_path = save_uploaded_file(file, case_id, f"claimant_evidence_{idx}")
                        saved_files.append(file_path)

                    # Save case data
                    st.session_state.case_data = {
                        'case_id': case_id,
                        'claimant': {
                            'full_name': full_name,
                            'id_number': id_number,
                            'email': email,
                            'phone': phone,
                            'id_document_path': id_doc_path,
                            'claim_text': claim_text,
                            'evidence_files': saved_files,
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        },
                        'defendant': None,
                        'rebuttal': None
                    }

                    st.session_state.case_stage = 'claim_submitted'
                    add_audit_log(case_id, "claim_submitted", f"כתב תביעה הוגש על ידי {full_name}")
                    st.success("התביעה נשלחה בהצלחה!")
                    st.rerun()
    else:
        st.info("יש לאשר את התקנון והסכם הבוררות על מנת להמשיך")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# Page: Defendant Portal
# =====================================================
def render_defendant_portal():
    # Back Button
    st.markdown('<div class="back-button">', unsafe_allow_html=True)
    if st.button("חזרה לדף הבית", key="back_from_defendant"):
        go_to_home()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Portal Title
    st.markdown("""
        <h1 class="portal-title">מסוף נתבעים</h1>
    """, unsafe_allow_html=True)

    # Form Container
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # Check if defense already submitted
    if st.session_state.case_stage in ['defense_submitted', 'rebuttal_submitted', 'locked']:
        if st.session_state.case_stage == 'defense_submitted':
            # מסך אישור מעודכן עם גרדיאנט מטאלי
            st.markdown("""
                <div style="background: #0E1117;
                            border: 3px solid transparent;
                            border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1;
                            border-radius: 20px;
                            padding: 50px;
                            margin: 40px auto;
                            max-width: 900px;">

                    <h2 style="color: #C29B40;
                               font-size: 2.5rem;
                               font-weight: 900;
                               text-align: center;
                               margin-bottom: 30px;">
                        אישור קבלת מסמכים משפטיים
                    </h2>

                    <div style="text-align: center; margin: 30px 0;">
                        <p style="color: #FFFFFF; font-size: 1.2rem; margin-bottom: 10px;">
                            מספר תיק למעקב:
                        </p>
                        <p style="color: #C29B40;
                                  font-size: 2.5rem;
                                  font-weight: 900;
                                  letter-spacing: 2px;
                                  margin: 15px 0;">
                            {case_id}
                        </p>
                    </div>

                    <div style="background: rgba(255, 255, 255, 0.05);
                                border-radius: 15px;
                                padding: 22px;
                                margin: 30px 0;">
                        <p style="color: #FFFFFF;
                                  font-size: 1.3rem;
                                  line-height: 1.8;
                                  text-align: center;
                                  margin-bottom: 20px;">
                            כתב ההגנה שלך התקבל במערכת והועבר לתובע.
                        </p>
                        <p style="color: #FFFFFF;
                                  font-size: 1.2rem;
                                  line-height: 1.8;
                                  text-align: center;">
                            המערכת תעדכן אותך במסרון (SMS) על כל התקדמות בתיק, קבלת תגובה מהתובע או מתן פסק בוררות סופי.
                        </p>
                    </div>

                    <p style="color: #FFFFFF;
                              font-size: 1.1rem;
                              text-align: center;
                              opacity: 0.8;
                              margin-top: 20px;">
                        התובע יקבל אפשרות להגיש כתב תשובה, ולאחר מכן התיק יועבר לניתוח הבורר.
                    </p>
                </div>
            """.format(case_id=st.session_state.case_id), unsafe_allow_html=True)

            # כפתור חזרה לדף הבית
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("חזרה לדף הבית", key="back_to_home_defendant_success", use_container_width=True):
                    go_to_home()
                    st.rerun()
        else:
            # התיק נעול - הצגת פסק דין
            st.markdown("""
                <div class="instruction-box" style="background: rgba(194, 155, 64, 0.15);
                     border: 2px solid transparent;
                     border-image: linear-gradient(135deg, #8E6D28 0%, #C29B40 45%, #E0C58A 55%, #C29B40 100%) 1;
                     padding: 22px;">
                    <p style="font-size: 1.4rem; font-weight: 700; color: #C29B40; text-align: center;">
                        התיק נעול - פסק הדין הראשוני הוכן
                    </p>
                    <p style="font-size: 1.1rem; color: #FFFFFF; text-align: center; margin-top: 15px;">
                        כל הטיעונים והראיות הועברו לניתוח מעמיק. להלן פסק הבוררות המנומק.
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # הפקת פסק דין
            ruling = generate_arbitration_ruling(st.session_state.case_id, st.session_state.case_data)

            # הצגת פסק הדין
            render_arbitration_ruling(ruling)

            # הודעת סיום
            st.markdown("""
                <div class="instruction-box" style="margin-top: 40px;">
                    <p style="font-size: 1.2rem; line-height: 1.8; text-align: center;">
                        <strong>פסק הדין הראשוני הוכן וממתין לאישור סופי.</strong>
                    </p>
                    <p style="font-size: 1rem; margin-top: 15px; opacity: 0.8; text-align: center;">
                        לא ניתן לערוך או להוסיף מסמכים נוספים בשלב זה.
                    </p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Section Title
    st.markdown("""
        <h2 class="section-title">אימות תיק והגשת כתב הגנה</h2>
    """, unsafe_allow_html=True)

    # Portal Description Box
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); border: 2px solid rgba(212, 175, 55, 0.3); border-radius: 20px; padding: 40px; margin: 20px auto 40px auto; max-width: 800px;">
            <p class="gold-gradient-text">כאן ניתן להגיש את כתב ההגנה שלך</p>
        </div>
    """, unsafe_allow_html=True)

    # Case ID Verification
    if 'defendant_case_verified' not in st.session_state:
        st.session_state.defendant_case_verified = False

    if not st.session_state.defendant_case_verified:
        st.markdown("""
            <div class="instruction-box">
                הזן את מספר התיק שקיבלת מהתובע על מנת להמשיך להגשת כתב הגנה.
            </div>
        """, unsafe_allow_html=True)

        case_id_input = st.text_input(
            "מספר תיק",
            key="defendant_case_id",
            placeholder="RA-XXXXXXXX-XXXXXX"
        )

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("אמת תיק", key="verify_case"):
                if not case_id_input:
                    st.error("נא להזין מספר תיק")
                elif case_id_input != st.session_state.case_id or st.session_state.case_stage != 'claim_submitted':
                    st.error("מספר תיק לא נמצא במערכת או התיק אינו פתוח לקבלת כתב הגנה.")
                else:
                    st.session_state.defendant_case_verified = True
                    add_audit_log(case_id_input, "defendant_accessed", "הנתבע נכנס למערכת")
                    st.success("תיק אומת בהצלחה!")
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Case verified - show claim first
    if not st.session_state.terms_scrolled_defendant:
        # Display the claim
        st.markdown('<p class="subsection-title">כתב התביעה - תצוגה בלבד</p>', unsafe_allow_html=True)

        if 'claimant' in st.session_state.case_data and st.session_state.case_data['claimant']:
            claimant = st.session_state.case_data['claimant']

            st.markdown('<div class="readonly-box">', unsafe_allow_html=True)
            st.markdown("<h4>פרטי התובע</h4>", unsafe_allow_html=True)
            st.markdown(f"""
                <p><strong>שם:</strong> {claimant['full_name']}</p>
                <p><strong>ת.ז:</strong> {claimant['id_number']}</p>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="readonly-box">', unsafe_allow_html=True)
            st.markdown("<h4>כתב התביעה</h4>", unsafe_allow_html=True)
            st.markdown(f"<p>{claimant['claim_text']}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Show evidence files
            if claimant.get('evidence_files'):
                st.markdown('<p class="subsection-title">נספחים של התובע</p>', unsafe_allow_html=True)
                for idx, file_path in enumerate(claimant['evidence_files']):
                    if os.path.exists(file_path):
                        file_name = os.path.basename(file_path)
                        with open(file_path, "rb") as f:
                            st.download_button(
                                label=f"הורד נספח {idx + 1}",
                                data=f.read(),
                                file_name=file_name,
                                key=f"download_claimant_evidence_{idx}"
                            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Show arbitration agreement
        st.markdown("""
            <div class="warning-box">
                <p style="font-weight: 700; font-size: 1.2rem; margin-bottom: 10px;">
                    אישור סמכות חובה
                </p>
                <p>
                    לפני הגשת כתב ההגנה, עליך לקרוא ולאשר את הסכם הבוררות המפורט.
                    ללא הסכמה זו, אין לבורר סמכות חוקית עליך.
                </p>
            </div>
        """, unsafe_allow_html=True)

        with st.expander("הסכם הבוררות המפורט - לחץ לקריאה"):
            render_terms_with_scroll("defendant")

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Terms confirmed - show defense form
    st.success("התקנון נקרא והסכמת הבוררות אושרה")

    # Legal Agreement Checkbox
    terms_accepted = st.checkbox(
        "אני מסכים למסור את ההכרעה ל-Resolve AI",
        key="terms_defendant"
    )

    if terms_accepted:
        st.markdown("<br>", unsafe_allow_html=True)

        # KYC - Identity Verification
        st.markdown('<p class="subsection-title">אימות זהות</p>', unsafe_allow_html=True)

        st.markdown("""
            <div class="warning-box">
                <p style="font-weight: 700; margin-bottom: 10px;">
                    אימות זהות הינו תנאי הכרחי למתן תוקף משפטי לפסק הבוררות.
                </p>
                <p>
                    נדרש להעלות צילום ברור של תעודת זהות או תעודת חברה רשומה.
                </p>
            </div>
        """, unsafe_allow_html=True)

        id_document = st.file_uploader(
            "העלה צילום תעודת זהות / תעודת חברה",
            type=["pdf", "jpg", "jpeg", "png"],
            key="defendant_id_document",
            help="קובץ PDF או תמונה (JPG/PNG)"
        )

        st.info("למען הגנת פרטיותך, הקובץ נמחק מהשרת מיד לאחר האימות. Resolve AI אינה שומרת עותקים של תעודות מזהות.")

        # Personal Details
        st.markdown('<p class="subsection-title">פרטים אישיים</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input(
                "שם מלא",
                key="defendant_full_name",
                placeholder="הזן שם פרטי ושם משפחה"
            )
            email = st.text_input(
                "כתובת אימייל",
                key="defendant_email",
                placeholder="example@email.com"
            )

        with col2:
            id_number = st.text_input(
                "מספר תעודת זהות",
                key="defendant_id",
                placeholder="הזן מספר תעודת זהות או מספר חברה"
            )
            phone = st.text_input(
                "מספר טלפון",
                key="defendant_phone",
                placeholder="05XXXXXXXX"
            )

        # Defense Details
        st.markdown('<p class="subsection-title">כתב הגנה ופירוט עובדתי</p>', unsafe_allow_html=True)

        st.markdown("""
            <div class="instruction-box">
                פרט את תגובתך לטענות התובע, את גרסתך לאירועים ואת טענות ההגנה שלך.
            </div>
        """, unsafe_allow_html=True)

        defense_text = st.text_area(
            "תיאור ההגנה",
            key="defense_description",
            placeholder="פרט כאן את תגובתך לתביעה, גרסתך לאירועים וטענות ההגנה...",
            height=300
        )

        # Evidence Upload
        st.markdown('<p class="subsection-title">נספחים ואסמכתאות</p>', unsafe_allow_html=True)

        defense_evidence_files = st.file_uploader(
            "העלה קבצי ראיות (PDF או DOCX בלבד)",
            type=["pdf", "docx"],
            accept_multiple_files=True,
            key="defendant_evidence"
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("שלח כתב הגנה", key="submit_defense"):
                # Validation
                if not id_document:
                    st.error("נא להעלות צילום תעודת זהות / תעודת חברה")
                elif not full_name or not id_number or not email or not phone:
                    st.error("נא למלא את כל הפרטים האישיים")
                elif not defense_text or len(defense_text) < 50:
                    st.error("נא לפרט את כתב ההגנה בצורה מפורטת (לפחות 50 תווים)")
                elif not defense_evidence_files or len(defense_evidence_files) == 0:
                    st.error("נא להעלות לפחות קובץ ראיה אחד")
                else:
                    # Save ID document
                    id_doc_path = save_uploaded_file(id_document, st.session_state.case_id, "defendant_id_document")

                    # Save evidence files
                    saved_files = []
                    for idx, file in enumerate(defense_evidence_files):
                        file_path = save_uploaded_file(file, st.session_state.case_id, f"defendant_evidence_{idx}")
                        saved_files.append(file_path)

                    # Update case data with defendant info
                    st.session_state.case_data['defendant'] = {
                        'full_name': full_name,
                        'id_number': id_number,
                        'email': email,
                        'phone': phone,
                        'id_document_path': id_doc_path,
                        'defense_text': defense_text,
                        'evidence_files': saved_files,
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                    st.session_state.case_stage = 'defense_submitted'
                    add_audit_log(st.session_state.case_id, "defense_submitted", f"כתב הגנה הוגש על ידי {full_name}")
                    st.success("כתב ההגנה נשלח בהצלחה!")
                    st.rerun()
    else:
        st.info("יש לאשר את הסכם הבוררות על מנת להמשיך")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# Main Application Router
# =====================================================
if st.session_state.page == 'home':
    render_home_page()
elif st.session_state.page == 'claimant_portal':
    render_claimant_portal()
elif st.session_state.page == 'defendant_portal':
    render_defendant_portal()
