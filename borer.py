import streamlit as st
import time

# הגדרות דף
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# אתחול session state
if 'show_about' not in st.session_state:
    st.session_state.show_about = False
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# ערכת צבעים מודרנית
primary_blue = "#1a4d5e"
secondary_blue = "#2a5f73"
accent_cyan = "#00d4ff"
accent_purple = "#667eea"
bg_light = "#f0f4f8"
card_bg = "#ffffff"
success_green = "#10b981"

# CSS מעוצב וחדשני
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');

    * {{
        font-family: 'Heebo', sans-serif;
        box-sizing: border-box;
    }}

    /* הסתרת אלמנטים של Streamlit */
    header, [data-testid="stHeader"], footer {{
        visibility: hidden !important;
        height: 0 !important;
    }}

    .block-container {{
        padding: 0px !important;
        max-width: 100% !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, {bg_light} 0%, #e0e7ff 100%) !important;
    }}

    /* Header מעוצב */
    .custom-header {{
        background: linear-gradient(135deg, {primary_blue} 0%, {secondary_blue} 100%);
        height: 90px;
        display: flex;
        align-items: center;
        padding: 0 60px;
        justify-content: space-between;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9999;
        box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }}

    .logo-section {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    .logo-img {{
        height: 65px;
        width: 65px;
        border-radius: 50%;
        box-shadow: 0 4px 15px rgba(0,212,255,0.3);
    }}

    .logo-text {{
        color: white;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }}

    .logo-ai {{
        color: {accent_cyan};
        text-shadow: 0 0 10px rgba(0,212,255,0.5);
    }}

    /* כפתור אודות */
    .about-btn {{
        background: rgba(255,255,255,0.15);
        border: 2px solid {accent_cyan};
        color: white;
        padding: 10px 30px;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }}

    .about-btn:hover {{
        background: {accent_cyan};
        color: {primary_blue};
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0,212,255,0.5);
    }}

    /* גוף האתר */
    .main-content {{
        margin-top: 100px;
        padding: 40px 10%;
        min-height: calc(100vh - 100px);
        direction: rtl;
    }}

    /* כותרת ראשית */
    .hero-section {{
        text-align: center;
        margin-bottom: 50px;
        animation: fadeIn 1s ease-in;
    }}

    .hero-title {{
        background: linear-gradient(135deg, {accent_cyan} 0%, {accent_purple} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 15px;
        text-shadow: 0 0 30px rgba(0,212,255,0.3);
    }}

    .hero-subtitle {{
        font-size: 1.5rem;
        color: #64748B;
        font-weight: 500;
    }}

    /* כרטיסי העלאה */
    .upload-card {{
        background: {card_bg};
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 2px solid transparent;
        position: relative;
        overflow: hidden;
    }}

    .upload-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, {accent_cyan}, {accent_purple});
    }}

    .upload-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        border-color: {accent_cyan};
    }}

    .card-header {{
        text-align: center;
        margin-bottom: 25px;
    }}

    .card-icon {{
        font-size: 3rem;
        margin-bottom: 15px;
    }}

    .card-title {{
        color: {primary_blue};
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 10px;
    }}

    .card-subtitle {{
        color: #94a3b8;
        font-size: 1.1rem;
    }}

    /* שדות טקסט */
    .stTextInput input {{
        border-radius: 15px !important;
        border: 2px solid #e2e8f0 !important;
        padding: 15px !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        text-align: right !important;
        direction: rtl !important;
    }}

    .stTextInput input:focus {{
        border-color: {accent_cyan} !important;
        box-shadow: 0 0 0 3px rgba(0,212,255,0.1) !important;
    }}

    /* העלאת קבצים */
    .stFileUploader {{
        background: #f8fafc !important;
        border-radius: 15px !important;
        border: 2px dashed #cbd5e1 !important;
        padding: 20px !important;
        transition: all 0.3s ease !important;
    }}

    .stFileUploader:hover {{
        border-color: {accent_cyan} !important;
        background: #f1f5f9 !important;
    }}

    /* כפתור ראשי */
    .main-button {{
        background: linear-gradient(135deg, {accent_purple} 0%, #764ba2 100%);
        color: white;
        padding: 20px 80px;
        border-radius: 50px;
        font-size: 1.5rem;
        font-weight: 700;
        border: none;
        box-shadow: 0 10px 30px rgba(102,126,234,0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        animation: pulse 2s infinite;
        display: block;
        margin: 50px auto;
        text-align: center;
    }}

    .main-button:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102,126,234,0.6);
    }}

    /* תוצאות */
    .result-card {{
        background: linear-gradient(135deg, {card_bg} 0%, #f8fafc 100%);
        border-radius: 25px;
        padding: 50px;
        margin-top: 30px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
        border-left: 5px solid {success_green};
        animation: slideIn 0.5s ease-out;
    }}

    .result-title {{
        color: {primary_blue};
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 30px;
        text-align: center;
    }}

    .result-section {{
        background: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-right: 4px solid {accent_cyan};
    }}

    .result-label {{
        color: {accent_cyan};
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 10px;
    }}

    .result-text {{
        color: #334155;
        font-size: 1.2rem;
        line-height: 1.8;
    }}

    .highlight {{
        background: linear-gradient(120deg, {accent_cyan}20 0%, {accent_purple}20 100%);
        padding: 3px 10px;
        border-radius: 5px;
        font-weight: 700;
        color: {primary_blue};
    }}

    /* אנימציות */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(-20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes slideIn {{
        from {{ opacity: 0; transform: translateX(50px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}

    @keyframes pulse {{
        0%, 100% {{ box-shadow: 0 10px 30px rgba(102,126,234,0.4); }}
        50% {{ box-shadow: 0 10px 40px rgba(102,126,234,0.6); }}
    }}

    /* Streamlit button override */
    .stButton>button {{
        background: linear-gradient(135deg, {accent_purple} 0%, #764ba2 100%) !important;
        color: white !important;
        padding: 20px 80px !important;
        border-radius: 50px !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(102,126,234,0.4) !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        display: block !important;
        margin: 50px auto !important;
    }}

    .stButton>button:hover {{
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 40px rgba(102,126,234,0.6) !important;
    }}

    /* Status spinner */
    .stStatus {{
        background: white !important;
        border-radius: 15px !important;
        padding: 20px !important;
    }}

    /* התאמה למובייל */
    @media (max-width: 768px) {{
        .hero-title {{ font-size: 2.5rem; }}
        .custom-header {{ padding: 0 20px; height: 70px; }}
        .logo-img {{ height: 50px; width: 50px; }}
        .main-content {{ padding: 30px 5%; }}
    }}
    </style>

    <div class="custom-header">
        <div class="logo-section">
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
            <div class="logo-text">Resolve <span class="logo-ai">AI</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# כותרת ראשית
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Resolve AI</h1>
    <p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>
</div>
""", unsafe_allow_html=True)

# כרטיסי העלאה
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="upload-card">
        <div class="card-header">
            <div class="card-icon">📝</div>
            <h2 class="card-title">צד תובע</h2>
            <p class="card-subtitle">הגש את כתב התביעה שלך</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    side_a_name = st.text_input("שם התובע", key="name_a", placeholder="הכנס שם מלא...", label_visibility="collapsed")
    file_a = st.file_uploader("העלה כתב תביעה (PDF)", type="pdf", key="file_a", label_visibility="collapsed")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="upload-card">
        <div class="card-header">
            <div class="card-icon">🛡️</div>
            <h2 class="card-title">צד נתבע</h2>
            <p class="card-subtitle">הגש את כתב ההגנה שלך</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    side_b_name = st.text_input("שם הנתבע", key="name_b", placeholder="הכנס שם מלא...", label_visibility="collapsed")
    file_b = st.file_uploader("העלה כתב הגנה (PDF)", type="pdf", key="file_b", label_visibility="collapsed")

    st.markdown("</div>", unsafe_allow_html=True)

# כפתור הפעלה
if st.button("🚀 בצע בוררות כעת"):
    if file_a and file_b and side_a_name and side_b_name:
        with st.status("🔍 מנתח מסמכים משפטיים באמצעות AI...", expanded=True) as status:
            st.write(f"📄 סורק את הטענות של {side_a_name}...")
            time.sleep(1.5)
            st.write(f"📋 מצליב נתונים מול כתב ההגנה של {side_b_name}...")
            time.sleep(1.5)
            st.write("⚖️ מנתח תקדימים משפטיים רלוונטיים...")
            time.sleep(1)
            st.write("✅ יוצר החלטת בוררות מקצועית...")
            time.sleep(1)
            status.update(label="✨ הניתוח הסתיים בהצלחה!", state="complete", expanded=False)

        st.session_state.show_result = True
    else:
        st.error("⚠️ נא למלא את כל השדות ולהעלות את המסמכים הנדרשים.")

# הצגת תוצאות
if st.session_state.show_result:
    st.markdown(f"""
    <div class="result-card">
        <h2 class="result-title">🎯 החלטת Resolve AI</h2>

        <div class="result-section">
            <div class="result-label">📌 נושא הסכסוך</div>
            <div class="result-text">אי-עמידה בלוחות זמנים של חוזה שירות בין הצדדים.</div>
        </div>

        <div class="result-section">
            <div class="result-label">🔍 ממצאים עיקריים</div>
            <div class="result-text">
                לאחר ניתוח מעמיק של המסמכים, נמצא כי <span class="highlight">{side_b_name}</span> חרג מהמועד
                המוסכם ב-<span class="highlight">14 ימי עסקים</span> ללא מתן הודעה מראש כנדרש.
                <br><br>
                הראיות שהוצגו על ידי <span class="highlight">{side_a_name}</span> מצביעות על נזק כלכלי ישיר
                הנובע מהעיכוב, כולל הפסד הכנסות והוצאות נוספות.
            </div>
        </div>

        <div class="result-section">
            <div class="result-label">⚖️ ההחלטה הסופית</div>
            <div class="result-text">
                בהתאם לסעיף 14 לחוזה ולאור הנזק שנגרם, נקבע כי <span class="highlight">{side_b_name}</span>
                ישלם פיצוי בסך <span class="highlight" style="font-size: 1.3em;">1,500 ₪</span>
                לטובת <span class="highlight">{side_a_name}</span>.
                <br><br>
                <b>תשלום יבוצע תוך 14 ימי עסקים מיום קבלת החלטה זו.</b>
            </div>
        </div>

        <div class="result-section" style="border-right: 4px solid #10b981; background: #f0fdf4;">
            <div class="result-label" style="color: #10b981;">✅ המלצות נוספות</div>
            <div class="result-text">
                • מומלץ לשני הצדדים לעדכן את החוזה ולהוסיף סעיפי קנסות ברורים יותר<br>
                • יש להקפיד על תקשורת בכתב בכל שינוי במועדים<br>
                • מומלץ להגדיר מנגנון התראות מוקדם למניעת סכסוכים עתידיים
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # כפתור לניתוח חדש
    if st.button("📝 בצע ניתוח חדש"):
        st.session_state.show_result = False
        st.rerun()

# פוטר
st.markdown("""
<br><br>
<div style='text-align: center; color: #94a3b8; font-size: 0.9rem; padding: 20px;'>
    <p>© 2024 Resolve AI - המערכת המתקדמת ביותר ליישוב סכסוכים</p>
    <p style='font-size: 0.8rem;'>מופעל ע"י בינה מלאכותית מתקדמת | מאובטח ומוצפן | תמיכה 24/7</p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
