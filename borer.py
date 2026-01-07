import streamlit as st
import time

# הגדרות דף - ניקוי שוליים מקסימלי
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הצבעים המדויקים מהסקיצה ששלחת
primary_blue = "#0A2647" # הכחול העמוק מה-Header
light_bg = "#F1F5F9"    # רקע הדף האפרפר-תכלת

st.markdown(f"""
    <style>
    /* 1. הסתרת רכיבי מערכת של Streamlit */
    header, [data-testid="stHeader"], footer {{visibility: hidden !important; height: 0px !important;}}
    .block-container {{padding: 0px !important; max-width: 100% !important;}}
    
    /* 2. Header מקצה לקצה */
    .header-bar {{
        background-color: {primary_blue};
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 80px;
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9999;
        direction: rtl;
    }}

    .nav-items {{
        display: flex;
        gap: 35px;
        color: white;
        font-size: 1.1rem;
        font-family: sans-serif;
    }}

    .logo-container {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}

    .logo-img {{
        height: 70px; /* לוגו גדול וברור */
    }}

    /* 3. גוף האתר - מירכוז מוחלט */
    .main-body {{
        background-color: {light_bg};
        min-height: 100vh;
        width: 100%;
        padding-top: 160px; /* רווח מה-Header */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        direction: rtl;
    }}

    .hero-title {{
        color: {primary_blue};
        font-size: 4.5rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        width: 100%;
    }}

    .hero-subtitle {{
        color: #475569;
        font-size: 1.6rem !important;
        margin-top: 10px !important;
        margin-bottom: 60px !important;
        width: 100%;
    }}

    /* 4. כרטיסי העלאת קבצים מעוצבים */
    .cards-wrapper {{
        display: flex;
        gap: 40px;
        justify-content: center;
        width: 90%;
        max-width: 1100px;
    }}

    .upload-card {{
        background: white;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        flex: 1;
        border: 1px solid #E2E8F0;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .card-title {{
        color: {primary_blue};
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 8px;
    }}

    .card-sub {{
        color: #64748B;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }}

    /* 5. כפתור הפעלה סגול ממורכז */
    .stButton {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 60px;
    }}

    .stButton>button {{
        background: linear-gradient(90deg, #7C3AED, #6366F1) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 20px 100px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(124, 58, 237, 0.3) !important;
        transition: transform 0.2s ease;
    }}

    .stButton>button:hover {{
        transform: translateY(-2px);
    }}
    </style>

    <div class="header-bar">
        <div class="nav-items">
            <span>אודות</span>
            <span>שירותים</span>
            <span>כתבות</span>
            <span>בורר</span>
        </div>
        <div class="logo-container">
            <span style="color: white; font-size: 2.2rem; font-weight: bold;">Resolve <span style="color: #22D3EE;">AI</span></span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
        </div>
    </div>
    """, unsafe_allow_html=True)

# מבנה גוף הדף
st.markdown('<div class="main-body">', unsafe_allow_html=True)

# כותרות ממורכזות
st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# אזור העלאת קבצים
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📝 צד א\' - תובע</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-sub">גרור לכאן כתב תביעה</div>', unsafe_allow_html=True)
    st.file_uploader("up1", key="tovea", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🛡️ צד ב\' - נתבע</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-subtitle">גרור לכאן כתב הגנה</div>', unsafe_allow_html=True)
    st.file_uploader("up2", key="nitba", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# כפתור סופי
if st.button("קבל הכרעת בורר עכשיו"):
    with st.spinner('הבינה המלאכותית מנתחת את המסמכים...'):
        time.sleep(3)
    st.success("הניתוח הושלם בהצלחה!")

st.markdown('</div>', unsafe_allow_html=True)
