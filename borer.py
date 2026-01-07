import streamlit as st
import time

# הגדרות דף בסיסיות
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# CSS מתקדם למירכוז, הגדלת לוגו ומניעת "הריבוע הלבן"
st.markdown("""
    <style>
    /* הסתרת Header מובנה של Streamlit */
    header, [data-testid="stHeader"] {visibility: hidden !important; height: 0px !important;}
    .block-container {padding: 0px !important; max-width: 100% !important;}
    
    /* ה-Header הכחול - מתיחה מלאה */
    .custom-header {
        background-color: #0A2647;
        width: 100%;
        height: 100px; /* הגדלתי מעט את גובה ה-Header */
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 60px;
        position: fixed;
        top: 0;
        z-index: 9999;
        box-sizing: border-box;
    }

    /* לוגו מוגדל עם הגנה מפני רקע לבן */
    .header-logo-img {
        height: 75px; /* הגדלת הלוגו באופן משמעותי */
        width: auto;
        mix-blend-mode: lighten; /* מעלים רקע לבן/כהה ומשלב אותו בכחול */
    }

    /* מירכוז גוף האתר */
    .main-content {
        margin-top: 140px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        width: 100%;
        direction: rtl;
    }

    .hero-title {
        color: #0A2647;
        font-size: 4rem !important;
        font-weight: 900 !important;
        margin-bottom: 0px !important;
        text-align: center;
        width: 100%;
    }

    .hero-subtitle {
        color: #64748B;
        font-size: 1.6rem !important;
        margin-top: 10px !important;
        margin-bottom: 50px !important;
        text-align: center;
        width: 100%;
    }

    /* מירכוז כותרות מעל אזורי העלאה */
    .upload-container {
        text-align: center;
        width: 100%;
    }
    
    .upload-label {
        font-size: 1.6rem;
        font-weight: bold;
        color: #0A2647;
        margin-bottom: 5px;
        display: block;
    }
    
    .upload-sublabel {
        color: #64748B;
        font-size: 1.1rem;
        margin-bottom: 15px;
        display: block;
    }

    /* מירכוז כפתור ההפעלה */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }

    .stButton>button {
        background: linear-gradient(90deg, #6366F1 0%, #34D399 100%) !important;
        color: white !important;
        border: none !important;
        padding: 18px 90px !important;
        border-radius: 50px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        box-shadow: 0 10px 25px rgba(99, 102, 241, 0.4) !important;
    }

    /* הבטחת מירכוז העמודות של Streamlit */
    [data-testid="stHorizontalBlock"] {
        justify-content: center !important;
        align-items: flex-start !important;
        gap: 50px !important;
    }
    </style>

    <div class="custom-header">
        <div style="color: white; display: flex; gap: 30px; font-weight: 500; font-size: 1.1rem;">
            <span>אודות</span>
            <span>צור קשר</span>
            <span>בורר</span>
        </div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <span style="color: white; font-size: 2.2rem; font-weight: 900;">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="header-logo-img">
        </div>
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# כותרות ממורכזות
st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# אזור העלאת מסמכים בשתי עמודות ממורכזות
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown('<span class="upload-label">📝 צד א\' - תובע</span>', unsafe_allow_html=True)
    st.markdown('<span class="upload-sublabel">גרור לכאן כתב תביעה</span>', unsafe_allow_html=True)
    st.file_uploader("", key="up_tovea", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    st.markdown('<span class="upload-label">🛡️ צד ב\' - נתבע</span>', unsafe_allow_html=True)
    st.markdown('<span class="upload-sublabel">גרור לכאן כתב הגנה</span>', unsafe_allow_html=True)
    st.file_uploader("", key="up_nitba", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# רווח קטן לפני הכפתור
st.markdown("<br>", unsafe_allow_html=True)

# כפתור הפעלה ממורכז
if st.button("קבל הכרעת בורר עכשיו"):
    with st.spinner('מעבד נתונים משפטיים...'):
        time.sleep(2)
    st.success("הניתוח הסתיים! ניתן לצפות בהכרעה.")
    st.balloons()

st.markdown('</div>', unsafe_allow_html=True)
