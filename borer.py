import streamlit as st
import time

# הגדרות דף בסיסיות
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הצבעים המקוריים שאהבת
primary_blue = "#1E3A8A" 
bg_color = "#F8FAFC"
accent_green = "#34D399"

# CSS ממוקד למירכוז המלל מעל הסקטורים וניקוי ה-Header
st.markdown(f"""
    <style>
    header {{visibility: hidden;}}
    .block-container {{padding: 0px !important;}}
    
    /* ה-Header המקורי */
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
    
    .logo-img {{
        height: 50px;
        filter: brightness(0) invert(1);
    }}

    .main-content {{
        margin-top: 120px;
        text-align: center;
        direction: rtl;
        padding: 0 10%;
    }}

    /* מירכוז כותרות הסקטורים */
    .sector-header {{
        text-align: center;
        margin-bottom: 10px;
    }}

    .stButton>button {{
        background: {accent_green} !important;
        color: #064E3B !important;
        border-radius: 50px !important;
        padding: 15px 60px !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border: none !important;
        margin-top: 40px;
    }}
    </style>

    <div class="custom-header">
        <div style="color: white; font-size: 1.5rem; font-weight: bold;">Resolve AI</div>
        <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown(f'<h1 style="color: {primary_blue}; font-size: 3rem;">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 1.4rem; color: #64748B;">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# פריסת הסקטורים עם מלל ממורכז
col1, space, col2 = st.columns([1, 0.2, 1])

with col1:
    st.markdown('<div class="sector-header">', unsafe_allow_html=True)
    st.markdown("### 📝 צד א' - תובע")
    st.markdown("<p>גרור לכאן כתב תביעה</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.file_uploader("", key="t1", label_visibility="collapsed")

with col2:
    st.markdown('<div class="sector-header">', unsafe_allow_html=True)
    st.markdown("### 🛡️ צד ב' - נתבע")
    st.markdown("<p>גרור לכאן כתב הגנה</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.file_uploader("", key="n1", label_visibility="collapsed")

# כפתור מרכזי
if st.button("קבל הכרעת בורר עכשיו"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם!")

st.markdown('</div>', unsafe_allow_html=True)
