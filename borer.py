import streamlit as st
import time

# הגדרות דף בסיסיות
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# ערכת צבעים חדשה - כחול-ירקרק (Teal/Cyan)
primary_blue = "#1a4d5e"  # כחול כהה
secondary_blue = "#2a5f73"  # כחול בינוני
accent_cyan = "#00d4ff"  # ציאן בהיר
bg_light = "#f0f4f8"  # רקע בהיר
card_bg = "#ffffff"  # רקע כרטיסים

# CSS מעוצב חדש
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700&display=swap');

    * {{
        font-family: 'Heebo', sans-serif;
    }}

    header {{visibility: hidden;}}
    .block-container {{padding: 0px !important;}}

    /* Header מעוצב */
    .custom-header {{
        background: linear-gradient(135deg, {primary_blue} 0%, {secondary_blue} 100%);
        height: 80px;
        display: flex;
        align-items: center;
        padding: 0 50px;
        justify-content: space-between;
        width: 100%;
        position: fixed;
        top: 0;
        z-index: 999;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }}

    .logo-section {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    .logo-img {{
        height: 50px;
        width: 50px;
        border-radius: 50%;
    }}

    .logo-text {{
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
    }}

    .logo-ai {{
        color: {accent_cyan};
    }}

    .nav-menu {{
        display: flex;
        gap: 30px;
        direction: rtl;
    }}

    .nav-item {{
        color: white;
        text-decoration: none;
        font-size: 1.1rem;
        font-weight: 500;
        transition: color 0.3s;
        cursor: pointer;
    }}

    .nav-item:hover {{
        color: {accent_cyan};
    }}

    .main-content {{
        margin-top: 120px;
        text-align: center;
        direction: rtl;
        padding: 40px 10%;
        background: {bg_light};
        min-height: calc(100vh - 120px);
    }}

    .hero-title {{
        color: {primary_blue};
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 15px;
    }}

    .hero-subtitle {{
        font-size: 1.3rem;
        color: #64748B;
        margin-bottom: 50px;
    }}

    /* כרטיסים מעוצבים */
    .card {{
        background: {card_bg};
        border-radius: 20px;
        padding: 40px 30px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: transform 0.3s, box-shadow 0.3s;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }}

    .card-title {{
        color: {primary_blue};
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 15px;
    }}

    .card-subtitle {{
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }}

    .card-button {{
        background: {primary_blue};
        color: white;
        padding: 12px 40px;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s;
    }}

    .card-button:hover {{
        background: {secondary_blue};
    }}

    /* כפתור מרכזי עם גרדיאנט */
    .stButton>button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 18px 80px !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        border: none !important;
        margin-top: 50px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s !important;
        animation: gradient 3s ease infinite !important;
    }}

    .stButton>button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }}

    @keyframes gradient {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    /* הסתרת אלמנטים של Streamlit */
    .stFileUploader {{
        display: none;
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

# כותרת ראשית
st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">תיווך בינה מלאכותית לפתרון סכסוכים מהיר ואובייקטיבי</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# כרטיסים
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown(f"""
    <div class="card">
        <h2 class="card-title">צד תובע</h2>
        <p class="card-subtitle">הגש תביעה משפטית</p>
        <button class="card-button">העלה כתב תביעה</button>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <h2 class="card-title">צד נתבע</h2>
        <p class="card-subtitle">הגש הגנה משפטית</p>
        <button class="card-button">העלה כתב הגנה</button>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# כפתור מרכזי
if st.button("תבצע סגילה אישית"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם!")

st.markdown('</div>', unsafe_allow_html=True)
