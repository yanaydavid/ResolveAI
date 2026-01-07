import streamlit as st
import time

# 1. הגדרות דף - ניקוי שוליים מקסימלי
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הצבעים המדויקים מהסקיצה
deep_blue = "#0A2647" # כחול כהה עמוק
soft_bg = "#F0F4F8"   # רקע אפור-תכלת רך מאוד
accent_color = "#34D399" # טורקיז

st.markdown(f"""
    <style>
    /* ביטול כל המרווחים הלבנים של Streamlit */
    [data-testid="stHeader"] {{display: none;}}
    .block-container {{
        padding: 0px !important;
        margin: 0px !important;
        max-width: 100% !important;
    }}
    
    /* ה-Header הכחול - נצמד למעלה ללא רווחים */
    .full-header {{
        background-color: {deep_blue};
        width: 100%;
        height: 75px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 50px;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1000;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }}

    .nav-items {{
        display: flex;
        gap: 25px;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 500;
        direction: rtl;
    }}

    .logo-section {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    /* טיפול בלוגו שייראה שקוף ולבן על הרקע הכהה */
    .logo-img {{
        height: 45px;
        mix-blend-mode: screen; /* גורם לרקע שחור/לבן להיעלם ולהשתלב */
        filter: brightness(0) invert(1); /* הופך ללבן נקי */
    }}

    /* תוכן מרכזי */
    .main-wrapper {{
        background-color: {soft_bg};
        min-height: 100vh;
        width: 100%;
        padding-top: 120px; /* רווח מה-Header */
        display: flex;
        flex-direction: column;
        align-items: center;
        direction: rtl;
    }}

    .hero-section {{
        text-align: center;
        margin-bottom: 40px;
    }}

    .hero-title {{
        color: {deep_blue};
        font-size: 3.8rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }}

    .hero-subtitle {{
        color: #475569;
        font-size: 1.5rem;
        margin-top: 10px;
    }}

    /* כרטיסי העלאה */
    .card-container {{
        display: flex;
        gap: 30px;
        justify-content: center;
        width: 80%;
        margin-top: 20px;
    }}

    .upload-card {{
        background: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        flex: 1;
        text-align: center;
        border: 1px solid #E2E8F0;
    }}

    /* כפתור הפעלה סופי */
    .stButton>button {{
        background: linear-gradient(135deg, #6366F1 0%, {accent_color} 100%) !important;
        color: white !important;
        border: none !important;
        padding: 18px 80px !important;
        border-radius: 50px !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        margin-top: 50px !important;
        box-shadow: 0 10px 20px rgba(99, 102, 241, 0.2) !important;
        transition: all 0.3s ease;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 25px rgba(99, 102, 241, 0.3) !important;
    }}
    </style>

    <div class="full-header">
        <div class="nav-items">
            <span>אודות</span>
            <span>שירותים</span>
            <span>צור קשר</span>
        </div>
        <div class="logo-section">
            <span style="color: white; font-size: 1.8rem; font-weight: bold;">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
        </div>
    </div>
    """, unsafe_allow_html=True)

# מבנה גוף הדף
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# יצירת העמודות להעלאת קבצים
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: {deep_blue};'>📝 צד א' - תובע</h2>", unsafe_allow_html=True)
    st.file_uploader("גרור או בחר כתב תביעה", key="up_tovea")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: {deep_blue};'>🛡️ צד ב' - נתבע</h2>", unsafe_allow_html=True)
    st.file_uploader("גרור או בחר כתב הגנה", key="up_nitba")
    st.markdown('</div>', unsafe_allow_html=True)

# כפתור ההפעלה
st.markdown('<div style="display: flex; justify-content: center; width: 100%;">', unsafe_allow_html=True)
if st.button("התחל תהליך בוררות חכם"):
    with st.spinner('הבינה המלאכותית מנתחת את המסמכים...'):
        time.sleep(3)
    st.balloons()
    st.success("הניתוח הושלם! ניתן להוריד את פסק הבורר.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
