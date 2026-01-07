import streamlit as st
import time

# הגדרות דף - חובה שיופיע ראשון
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# קישור ישיר ללוגו שלך ב-GitHub
logo_url = "https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png"

# עיצוב CSS לניקוי שוליים והצמדת הפס הכחול למעלה
st.markdown("""
    <style>
    /* הסתרת כותרות ברירת מחדל של Streamlit */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* הצמדת התוכן לקצה העליון */
    .block-container {
        padding: 0px !important;
        margin: 0px !important;
    }

    /* הפס הכחול העליון - Navbar */
    .nav-bar {
        background-color: #1a3a5a;
        padding: 10px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        width: 100%;
        height: 80px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .nav-logo-section {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .nav-links {
        display: flex;
        gap: 30px;
        font-weight: 500;
    }

    /* גוף האתר */
    .main-content {
        padding: 50px 10%;
        direction: rtl;
        text-align: center;
        background-color: #f4f7f9;
        min-height: 100vh;
    }
    
    .main-title {
        color: #1a3a5a;
        font-size: 3rem;
        margin-bottom: 10px;
        font-weight: bold;
    }

    /* עיצוב תיבות העלאת הקבצים */
    .upload-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-top: 5px solid #1a3a5a;
    }
    </style>
    """, unsafe_allow_html=True)

# יצירת ה-Navbar הכחול
st.markdown(f"""
    <div class="nav-bar">
        <div class="nav-links">
            <span>אודות</span>
            <span>שירותים</span>
            <span>צור קשר</span>
        </div>
        <div class="nav-logo-section">
            <span style="font-size: 24px; font-weight: bold;">Resolve AI</span>
            <img src="{logo_url}" width="50">
        </div>
    </div>
    """, unsafe_allow_html=True)

# תחילת תוכן האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.3rem; color: #555;">יישוב סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# פריסת עמודות להעלאת קבצים
col1, space, col2 = st.columns([1, 0.2, 1])

with col1:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown("### 📝 צד א' - תובע")
    tovea = st.file_uploader("גרור לכאן כתב תביעה", key="up1")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-card">', unsafe_allow_html=True)
    st.markdown("### 🛡️ צד ב' - נתבע")
    nitba = st.file_uploader("גרור לכאן כתב הגנה", key="up2")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("התחל תהליך בוררות"):
    if tovea and nitba:
        with st.spinner('מנתח מסמכים משפטיים...'):
            time.sleep(3)
        st.success("הניתוח הושלם בהצלחה!")
    else:
        st.error("יש להעלות מסמכים משני הצדדים כדי להמשיך.")

st.markdown('</div>', unsafe_allow_html=True)
