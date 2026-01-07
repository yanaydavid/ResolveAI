import streamlit as st
import time

# הגדרות דף - חייב להיות ראשון
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# עיצוב ה-Header והאלמנטים לפי התמונה שבחרת
st.markdown("""
    <style>
    header {visibility: hidden;}
    .block-container {padding: 0px !important;}
    
    /* ה-Header הכחול העמוק מהתמונה */
    .custom-header {
        background-color: #0A2647;
        height: 80px;
        display: flex;
        align-items: center;
        padding: 0 50px;
        justify-content: space-between;
        width: 100%;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
        gap: 15px;
        color: white;
        font-family: sans-serif;
    }

    .main-body {
        text-align: center;
        padding-top: 60px;
        background-color: #F8FAFC;
        min-height: 100vh;
        direction: rtl;
    }

    .hero-title {
        color: #0A2647;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        color: #64748B;
        font-size: 1.4rem;
        margin-bottom: 50px;
    }

    /* כרטיסי העלאת קבצים */
    .upload-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border-top: 5px solid #0A2647;
    }
    
    /* כפתור הפעולה הסגול/טורקיז מהתמונה */
    .stButton>button {
        background: linear-gradient(90deg, #6366F1, #34D399) !important;
        color: white !important;
        border: none !important;
        padding: 15px 80px !important;
        border-radius: 50px !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        box-shadow: 0 10px 15px rgba(99, 102, 241, 0.3) !important;
    }
    </style>

    <div class="custom-header">
        <div style="display: flex; gap: 30px; color: white; font-weight: 500;">
            <span>צור קשר</span>
            <span>אודות</span>
        </div>
        <div class="logo-container">
            <span style="font-size: 1.8rem; font-weight: bold;">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" style="height: 50px; filter: brightness(0) invert(1);">
        </div>
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-body">', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# עמודות
col1, space, col2 = st.columns([1, 0.2, 1])

with col1:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown("### 📝 צד א' - תובע")
    st.file_uploader("העלה כתב תביעה", key="p1")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown("### 🛡️ צד ב' - נתבע")
    st.file_uploader("העלה כתב הגנה", key="d1")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("קבל הכרעת בורר עכשיו"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם!")

st.markdown('</div>', unsafe_allow_html=True)
