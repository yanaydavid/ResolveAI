import streamlit as st
import time

# הגדרות דף בסיסיות
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# ערכת צבעים מדויקת לפי התמונה
primary_blue = "#1a4d5e"  # כחול כהה ל-header
secondary_blue = "#2a5f73"  # כחול בינוני לגרדיאנט
accent_cyan = "#00d4ff"  # ציאן בהיר ל-AI
bg_light = "#e8ecf0"  # רקע בהיר אפרפר
card_bg = "#ffffff"  # לבן לכרטיסים

# CSS מעוצב ומותאם לעברית
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
        display: none !important;
    }}

    .block-container {{
        padding: 0px !important;
        max-width: 100% !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: {bg_light} !important;
    }}

    /* מניעת מלבנים לבנים בתצוגות שונות */
    .main, [data-testid="stApp"], body {{
        background-color: {bg_light} !important;
    }}

    /* Header מעוצב בכחול כהה */
    .custom-header {{
        background: linear-gradient(135deg, {primary_blue} 0%, {secondary_blue} 100%);
        height: 85px;
        display: flex;
        align-items: center;
        padding: 0 60px;
        justify-content: space-between;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9999;
        box-shadow: 0 2px 15px rgba(0,0,0,0.1);
    }}

    .logo-section {{
        display: flex;
        align-items: center;
        gap: 15px;
        direction: ltr;
    }}

    .logo-img {{
        height: 55px;
        width: 55px;
        border-radius: 50%;
    }}

    .logo-text {{
        color: white;
        font-size: 1.9rem;
        font-weight: 700;
    }}

    .logo-ai {{
        color: {accent_cyan};
    }}

    .nav-menu {{
        display: flex;
        gap: 35px;
        direction: rtl;
    }}

    .nav-item {{
        color: white;
        text-decoration: none;
        font-size: 1.15rem;
        font-weight: 500;
        transition: color 0.3s ease;
        cursor: pointer;
    }}

    .nav-item:hover {{
        color: {accent_cyan};
    }}

    /* גוף האתר - ממורכז לחלוטין */
    .main-content {{
        margin-top: 130px;
        text-align: center;
        direction: rtl;
        padding: 50px 10%;
        background: {bg_light};
        min-height: calc(100vh - 130px);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* כותרת ראשית - ממורכזת */
    .hero-title {{
        color: {primary_blue};
        font-size: 3.8rem;
        font-weight: 900;
        margin: 0 auto 15px auto;
        text-align: center;
        width: 100%;
    }}

    /* כותרת משנה - ממורכזת */
    .hero-subtitle {{
        font-size: 1.35rem;
        color: #64748B;
        margin: 0 auto 60px auto;
        text-align: center;
        width: 100%;
    }}

    /* כרטיסים מעוצבים */
    .card {{
        background: {card_bg};
        border-radius: 20px;
        padding: 45px 35px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }}

    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 35px rgba(0,0,0,0.15);
    }}

    /* כותרת בכרטיס - ממורכזת */
    .card-title {{
        color: {primary_blue};
        font-size: 1.9rem;
        font-weight: 700;
        margin-bottom: 15px;
        text-align: center;
        width: 100%;
    }}

    /* כותרת משנה בכרטיס - ממורכזת */
    .card-subtitle {{
        color: #94a3b8;
        font-size: 1.15rem;
        margin-bottom: 30px;
        text-align: center;
        width: 100%;
    }}

    .card-button {{
        background: {primary_blue};
        color: white;
        padding: 13px 45px;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }}

    .card-button:hover {{
        background: {secondary_blue};
        transform: scale(1.05);
    }}

    /* מירכוז עמודות Streamlit */
    [data-testid="column"] {{
        display: flex;
        justify-content: center;
    }}

    /* כפתור מרכזי עם גרדיאנט סגול */
    .stButton {{
        display: flex;
        justify-content: center;
        width: 100%;
    }}

    .stButton>button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 20px 90px !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        border: none !important;
        margin: 60px auto 0 auto !important;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        animation: gradient 3s ease infinite !important;
        display: block;
    }}

    .stButton>button:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6) !important;
    }}

    @keyframes gradient {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    /* הסתרת אלמנטי העלאה של Streamlit */
    .stFileUploader {{
        display: none;
    }}

    /* התאמה למסכים קטנים */
    @media (max-width: 768px) {{
        .custom-header {{
            padding: 0 20px;
        }}

        .hero-title {{
            font-size: 2.5rem;
        }}

        .nav-menu {{
            gap: 15px;
        }}

        .nav-item {{
            font-size: 0.95rem;
        }}
    }}
    </style>

    <div class="custom-header">
        <div class="logo-section">
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
            <div class="logo-text">Resolve <span class="logo-ai">AI</span></div>
        </div>
        <div class="nav-menu">
            <div class="nav-item">אתר</div>
            <div class="nav-item">עשה</div>
            <div class="nav-item">כניסה</div>
            <div class="nav-item">בורר</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# כותרת ראשית וכותרת משנה - ממורכזות
st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">תיווך בינה מלאכותית לפתרון סכסוכים מהיר ואובייקטיבי</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# כרטיסים - ממורכזים
col1, space, col2 = st.columns([1, 0.15, 1])

with col1:
    st.markdown("""
    <div class="card">
        <h2 class="card-title">צד תובע</h2>
        <p class="card-subtitle">הגש תביעה משפטית</p>
        <button class="card-button">העלה כתב תביעה</button>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2 class="card-title">צד נתבע</h2>
        <p class="card-subtitle">הגש הגנה משפטית</p>
        <button class="card-button">העלה כתב הגנה</button>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# כפתור מרכזי עם גרדיאנט
if st.button("תבצע סגילה אישית"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם!")

st.markdown('</div>', unsafe_allow_html=True)
