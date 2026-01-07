import streamlit as st
import time

# הגדרות דף בסיסיות
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הצבעים המדויקים מהעיצוב שבחרת
primary_blue = "#1E3A8A"  # כחול עמוק ל-Header
bg_color = "#F8FAFC"      # רקע אפור בהיר מאוד
accent_green = "#34D399"  # טורקיז לכפתורים

# קוד CSS להטמעת העיצוב המדויק
st.markdown(f"""
    <style>
    /* הסתרת אלמנטים של המערכת */
    header {{visibility: hidden;}}
    .block-container {{padding: 0px !important;}}
    
    /* ה-Header הכחול */
    .custom-header {{
        background-color: {primary_blue};
        height: 80px;
        display: flex;
        align-items: center;
        padding: 0 40px;
        justify-content: space-between;
        width: 100%;
        position: fixed;
        top: 0;
        z-index: 999;
    }}
    
    /* עיבוד לוגו שיהיה שקוף */
    .logo-img {{
        height: 50px;
        filter: brightness(0) invert(1); /* הופך את הלוגו ללבן נקי ושקוף */
    }}

    /* מרכז הדף */
    .main-content {{
        margin-top: 120px;
        text-align: center;
        direction: rtl;
        padding: 0 15%;
    }}

    .main-title {{
        color: {primary_blue};
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 10px;
    }}

    .sub-title {{
        color: #64748B;
        font-size: 1.4rem;
        margin-bottom: 50px;
    }}

    /* תיבות העלאה מעוצבות */
    .upload-box {{
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        border: 1px solid #E2E8F0;
        transition: 0.3s;
    }}
    
    /* כפתור הפעולה */
    .stButton>button {{
        background: {accent_green} !important;
        color: #064E3B !important;
        border-radius: 50px !important;
        padding: 15px 60px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none !important;
        margin-top: 40px;
        box-shadow: 0 4px 15px rgba(52, 211, 153, 0.3);
    }}
    </style>

    <div class="custom-header">
        <div style="color: white; font-size: 1.5rem; font-weight: bold;">Resolve AI</div>
        <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# פריסת תיבות העלאה
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    st.markdown("### 📝 צד א' - תובע")
    st.file_uploader("גרור לכאן כתב תביעה", key="t1")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="upload-box">', unsafe_allow_html=True)
    st.markdown("### 🛡️ צד ב' - נתבע")
    st.file_uploader("גרור לכאן כתב הגנה", key="n1")
    st.markdown('</div>', unsafe_allow_html=True)

# כפתור מרכזי
if st.button("קבל הכרעת בורר עכשיו"):
    with st.spinner('מנתח מסמכים משפטיים...'):
        time.sleep(3)
    st.success("הניתוח הושלם! ניתן לצפות בתוצאות.")

st.markdown('</div>', unsafe_allow_html=True)
