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

    /* Global RTL Settings */
    * {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* Hide Streamlit Branding */
    header[data-testid="stHeader"],
    footer,
    #MainMenu {
        visibility: hidden;
        height: 0;
    }

    .block-container {
        padding-top: 2rem !important;
        max-width: 100% !important;
    }

    /* Background - Deep Navy */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0A2647 0%, #144272 50%, #205295 100%);
        min-height: 100vh;
    }

    /* Main Content Container */
    .main-content {
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Header Title */
    .main-title {
        color: white;
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 80px;
        margin-top: 40px;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }

    /* Portal Title */
    .portal-title {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 50px;
        margin-top: 20px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    /* Column Cards */
    .column-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 60px 40px;
        text-align: center;
        transition: all 0.4s ease;
        border: 2px solid transparent;
        backdrop-filter: blur(10px);
        min-height: 400px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .column-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(218, 165, 32, 0.5);
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    }

    .column-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 40px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }

    /* Form Container */
    .form-container {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 50px;
        margin: 30px auto;
        max-width: 900px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(218, 165, 32, 0.3);
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }

    .section-title {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    .subsection-title {
        color: #FFD700;
        font-size: 1.5rem;
        font-weight: 600;
        text-align: right;
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(218, 165, 32, 0.3);
        padding-bottom: 10px;
    }

    /* Terms Container */
    .terms-container {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(218, 165, 32, 0.4);
        border-radius: 15px;
        padding: 30px;
        margin: 30px 0;
        max-height: 500px;
        overflow-y: scroll;
        direction: rtl;
        text-align: right;
    }

    .terms-container::-webkit-scrollbar {
        width: 10px;
    }

    .terms-container::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }

    .terms-container::-webkit-scrollbar-thumb {
        background: rgba(218, 165, 32, 0.6);
        border-radius: 10px;
    }

    .terms-container::-webkit-scrollbar-thumb:hover {
        background: rgba(218, 165, 32, 0.8);
    }

    .terms-title {
        color: #FFD700;
        font-size: 1.8rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 2px solid rgba(218, 165, 32, 0.5);
        padding-bottom: 15px;
    }

    .terms-section {
        color: white;
        margin-bottom: 25px;
        line-height: 1.9;
        font-size: 1.05rem;
    }

    .terms-section h3 {
        color: #FFD700;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 15px;
        margin-top: 20px;
    }

    .terms-section p {
        margin-bottom: 12px;
        text-align: right;
        direction: rtl;
    }

    .scroll-instruction {
        color: #FFD700;
        text-align: center;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 15px;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }

    /* Case ID Display */
    .case-id-box {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin: 30px 0;
        box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);
    }

    .case-id-title {
        font-size: 1.3rem;
        margin-bottom: 10px;
        opacity: 0.9;
    }

    .case-id-number {
        font-size: 3.5rem;
        font-weight: 900;
        margin: 0;
        letter-spacing: 3px;
    }

    /* Success Message Box */
    .success-box {
        background: rgba(16, 185, 129, 0.2);
        border: 2px solid #10b981;
        border-radius: 15px;
        padding: 25px;
        margin: 30px 0;
        color: white;
        text-align: center;
    }

    /* Warning Box */
    .warning-box {
        background: rgba(239, 68, 68, 0.15);
        border: 2px solid rgba(239, 68, 68, 0.5);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        color: white;
        font-size: 1.1rem;
        line-height: 1.8;
        direction: rtl;
        text-align: right;
    }

    /* Instruction Box */
    .instruction-box {
        background: rgba(255, 193, 7, 0.15);
        border: 2px solid rgba(255, 193, 7, 0.5);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        color: white;
        font-size: 1.1rem;
        line-height: 1.8;
        direction: rtl;
        text-align: right;
    }

    /* Read-Only Box */
    .readonly-box {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(100, 116, 139, 0.5);
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        color: white;
        direction: rtl;
        text-align: right;
        max-height: 400px;
        overflow-y: auto;
    }

    .readonly-box h4 {
        color: #FFD700;
        font-size: 1.3rem;
        margin-bottom: 15px;
        border-bottom: 1px solid rgba(218, 165, 32, 0.3);
        padding-bottom: 10px;
    }

    .readonly-box p {
        line-height: 1.8;
        font-size: 1.05rem;
        white-space: pre-wrap;
    }

    /* Locked Case Box */
    .locked-box {
        background: rgba(100, 116, 139, 0.2);
        border: 3px solid rgba(100, 116, 139, 0.6);
        border-radius: 15px;
        padding: 30px;
        margin: 30px 0;
        color: white;
        text-align: center;
    }

    /* Luxury Buttons */
    .stButton > button {
        background: transparent !important;
        color: white !important;
        border: 3px solid #DAA520 !important;
        border-radius: 50px !important;
        padding: 20px 60px !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 0 30px rgba(218, 165, 32, 0.3) !important;
        letter-spacing: 1px !important;
        width: 100% !important;
        max-width: 400px !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #DAA520, #FFD700) !important;
        color: #0A2647 !important;
        border-color: #FFD700 !important;
        box-shadow: 0 0 50px rgba(218, 165, 32, 0.6) !important;
        transform: scale(1.05) !important;
    }

    .stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Text Inputs */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(218, 165, 32, 0.4) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 15px 20px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #DAA520 !important;
        box-shadow: 0 0 20px rgba(218, 165, 32, 0.4) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }

    /* Text Area */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(218, 165, 32, 0.4) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 15px 20px !important;
        direction: rtl !important;
        text-align: right !important;
        min-height: 200px !important;
    }

    .stTextArea textarea:focus {
        border-color: #DAA520 !important;
        box-shadow: 0 0 20px rgba(218, 165, 32, 0.4) !important;
    }

    /* Labels */
    .stTextInput label, .stTextArea label {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    /* File Uploader */
    .stFileUploader {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(218, 165, 32, 0.4) !important;
        border-radius: 12px !important;
        padding: 20px !important;
    }

    .stFileUploader label {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    /* Checkbox */
    .stCheckbox {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 12px;
        border: 2px solid rgba(218, 165, 32, 0.3);
        margin: 30px 0;
    }

    .stCheckbox label {
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        line-height: 1.8 !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(218, 165, 32, 0.4) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }

    /* Warning/Info boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 12px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* RTL Columns */
    [data-testid="column"] {
        direction: rtl;
        text-align: center;
    }

    /* Back Button Style */
    .back-button {
        margin-bottom: 30px;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
            margin-bottom: 40px;
        }

        .portal-title {
            font-size: 2rem;
        }

        .column-title {
            font-size: 1.8rem;
        }

        .column-card {
            padding: 40px 20px;
            min-height: 300px;
        }

        .form-container {
            padding: 30px 20px;
        }

        .terms-container {
            padding: 20px;
            max-height: 400px;
        }

        .case-id-number {
            font-size: 2.5rem !important;
        }

        .stButton > button {
            font-size: 1.2rem !important;
            padding: 15px 40px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================
# Terms and Conditions - Full Legal Text
# =====================================================
TERMS_HTML = """
<div class="terms-title">
    תקנון, תנאי שימוש והסכם בוררות מחייב – Resolve AI
</div>

<div class="terms-section">
    <h3>1. הגדרת ההסכם וסמכות הכרעה</h3>
    <p>
        המשתמשים (להלן: "הצדדים") נותנים בזאת את הסכמתם המלאה, המפורשת והבלתי חוזרת למסור כל סכסוך ביניהם להכרעה בלעדית של מערכת Resolve AI (להלן: "הבורר").
    </p>
    <p>
        הצדדים מאשרים כי ידוע להם והם מסכימים לכך שהבורר הינו מערכת בינה מלאכותית המקבלת החלטות על בסיס ניתוח לוגי של טענות וראיות, ללא התערבות אנושית בזמן אמת.
    </p>
</div>

<div class="terms-section">
    <h3>2. כפיפות לחוק הבוררות וסמכויות</h3>
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
    <h3>3. פטור מסדרי דין ודיני ראיות</h3>
    <p>
        בהתאם לסמכות לפי החוק, הבורר לא יהיה קשור בסדרי הדין האזרחיים או בדיני הראיות.
    </p>
    <p>
        הבורר יפסוק על פי שיקול דעת אובייקטיבי, עקרונות הצדק הטבעי והמסמכים שהוגשו על ידי הצדדים בלבד.
    </p>
</div>

<div class="terms-section">
    <h3>4. חובת גילוי ושלמות המידע</h3>
    <p>
        כל צד מתחייב להעלות את כל הראיות והטענות שברשותו. אי-העלאת ראיה תהווה ויתור על הזכות להסתמך עליה בעתיד.
    </p>
    <p>
        העלאת מידע כוזב או מסמכים מזויפים מהווה עילה לביטול הפסק ולחיוב בפיצויים.
    </p>
</div>

<div class="terms-section">
    <h3>5. סופיות הדיון וויתור על ערעור</h3>
    <p>
        הצדדים מוותרים על זכות הערעור על פסק הבוררות בכל ערכאה שהיא, למעט בעילות המצומצמות המנויות בסעיף 24 לחוק הבוררות.
    </p>
    <p>
        מוסכם כי השימוש בבינה מלאכותית כבורר אינו מהווה כשלעצמו עילה לביטול הפסק לפי סעיף 24.
    </p>
</div>

<div class="terms-section">
    <h3>6. אבטחה, אימות וחתימה דיגיטלית</h3>
    <p>
        הצדדים מסכימים כי הפקת קוד זיהוי דיגיטלי (Hash) המוטמע במסמך מהווה חתימה אלקטרונית מאושרת לפי חוק חתימה אלקטרונית, התשס"א-2001.
    </p>
    <p>
        קוד זה מהווה ראיה חלוטה לשלמות המסמך ומניעת כל שינוי בו לאחר הפקתו.
    </p>
</div>

<div class="terms-section">
    <h3>7. סמכות שיפוט שיורית</h3>
    <p>
        כל פנייה לבית משפט בבקשה לסעד זמני או לאישור/ביטול הפסק תוגש לבית המשפט המוסמך במחוז תל אביב בלבד.
    </p>
</div>

<div class="terms-section">
    <h3>8. הגנת פרטיות ואימות זהות</h3>
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
    אנא גלול עד סוף התקנון לפני האישור
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

    # Check if case is locked
    if st.session_state.case_stage in ['rebuttal_submitted', 'locked']:
        st.markdown("""
            <div class="locked-box">
                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">התיק נעול</h2>
                <p style="font-size: 1.3rem;">
                    כל הטיעונים והראיות הועברו לניתוח מעמיק של הבורר לצורך הפקת פסק דין מנומק.
                </p>
                <p style="font-size: 1.1rem; margin-top: 20px; opacity: 0.9;">
                    לא ניתן לערוך או להוסיף מסמכים נוספים בשלב זה.
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Check if claim already submitted
    if st.session_state.case_stage == 'claim_submitted':
        st.markdown(f"""
            <div class="case-id-box">
                <h2 style="font-size: 2.5rem; margin-bottom: 20px;">כתב התביעה הוגש בהצלחה</h2>
                <p class="case-id-title">מספר תיק</p>
                <h1 class="case-id-number">{st.session_state.case_id}</h1>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="success-box">
                <p style="font-size: 1.2rem; font-weight: 700; margin-bottom: 15px;">
                    הודעת SMS רשמית הכוללת הזמנה לדין נשלחה כעת לנתבע
                </p>
                <p style="font-size: 1rem; opacity: 0.9;">
                    המערכת שלחה הודעה אוטומטית עם פרטי התיק והזמנה להגיש כתב הגנה.
                </p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="instruction-box">
                <p style="font-size: 1.3rem; font-weight: 700; margin-bottom: 15px;">
                    שלב הבא - העברת הפרטים לנתבע
                </p>
                <p>
                    עליך להעביר את מספר התיק הבא לנתבע:
                </p>
                <p style="font-size: 1.5rem; font-weight: 800; text-align: center; margin: 20px 0; color: #FFD700;">
                    {case_id}
                </p>
                <p>
                    הנתבע יזין את מספר התיק במסוף הנתבעים על מנת להגיש את כתב ההגנה שלו.
                </p>
                <p style="margin-top: 20px; font-weight: 600;">
                    לאחר שהנתבע יגיש את כתב ההגנה, תקבל הזדמנות להגיש כתב תשובה.
                </p>
            </div>
        """.format(case_id=st.session_state.case_id), unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Section Title
    st.markdown("""
        <h2 class="section-title">רישום תובע והגשת תביעה</h2>
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
            st.markdown("""
                <div class="success-box">
                    <h2 style="font-size: 2.5rem; margin-bottom: 20px;">כתב ההגנה הוגש בהצלחה</h2>
                    <p style="font-size: 1.3rem;">
                        כתב ההגנה שלך הועבר לתובע.
                    </p>
                    <p style="font-size: 1.1rem; margin-top: 15px;">
                        התובע יקבל אפשרות להגיש כתב תשובה, ולאחר מכן התיק יועבר לניתוח הבורר.
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="locked-box">
                    <h2 style="font-size: 2.5rem; margin-bottom: 20px;">התיק נעול</h2>
                    <p style="font-size: 1.3rem;">
                        כל הטיעונים והראיות הועברו לניתוח מעמיק של הבורר לצורך הפקת פסק דין מנומק.
                    </p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        return

    # Section Title
    st.markdown("""
        <h2 class="section-title">אימות תיק והגשת כתב הגנה</h2>
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
