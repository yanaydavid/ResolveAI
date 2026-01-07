import streamlit as st
import time

# הגדרות דף - חייב להיות ראשון
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הזרקת CSS אגרסיבי לביטול השוליים והפס הלבן
st.markdown("""
    <style>
    /* הסתרת ה-Header המובנה של Streamlit */
    header, [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* ביטול שוליים עליונים של התוכן */
    .main .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    /* הפס הכחול העמוק - נצמד לראש הדף באבסולוטיות */
    .custom-navbar {
        background-color: #0A2647;
        width: 100%;
        height: 80px;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 50px;
        z-index: 9999;
        box-sizing: border-box;
    }
    
    /* לוגו שקוף ולבן */
    .navbar-logo {
        height: 50px;
        filter: brightness(0) invert(1);
        mix-blend-mode: screen;
    }

    .navbar-text {
        color: white;
        font-size: 1.8rem;
        font-weight: bold;
        font-family: sans-serif;
    }

    /* גוף האתר - מורד למטה כדי לא להיבלע תחת ה-Navbar */
    .main-content {
        margin-top: 100px;
        text-align: center;
        direction: rtl;
        font-family: 'Assistant', sans-serif;
    }

    .hero-title {
        color: #0A2647;
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 0;
    }

    .hero-subtitle {
        color: #64748B;
        font-size: 1.5rem;
        margin-top: 0;
        margin-bottom: 50px;
    }

    /* עיצוב כפתור הטורקיז */
    div.stButton > button {
        background: linear-gradient(90deg, #1E3A8A, #34D399) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 80px !important;
        font-size: 1.3rem !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    </style>

    <div class="custom-navbar">
        <div style="color: rgba(255,255,255,0.8); display: flex; gap: 20px; font-weight: 500;">
            <span>אודות</span>
            <span>צור קשר</span>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <span class="navbar-text">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="navbar-logo">
        </div>
    </div>
    """, unsafe_allow_html=True)

# תוכן האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# אזור העלאת קבצים
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📝 צד א' - תובע")
    st.file_uploader("גרור לכאן כתב תביעה", key="p1")

with col2:
    st.markdown("### 🛡️ צד ב' - נתבע")
    st.file_uploader("גרור לכאן כתב הגנה", key="d1")

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("התחל תהליך בוררות"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם!")

st.markdown('</div>', unsafe_allow_html=True)
