import streamlit as st
import time

# הגדרות דף בסיסיות
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הצבעים המדויקים מהסקיצה שלך
deep_blue = "#0A2647" 
bg_color = "#F8FAFC"

# הזרקת ה-CSS לתיקון המירכוז, ה-Header והלוגו
st.markdown(f"""
    <style>
    /* הסתרת אלמנטים מובנים של Streamlit שיוצרים רווחים */
    header, [data-testid="stHeader"] {{visibility: hidden !important; height: 0px !important;}}
    .block-container {{padding: 0px !important; max-width: 100% !important;}}
    
    /* ה-Header הכחול - נמתח מקצה לקצה */
    .custom-header {{
        background-color: {deep_blue};
        width: 100%;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 50px;
        position: fixed;
        top: 0;
        z-index: 9999;
        box-sizing: border-box;
    }}

    /* מירכוז מוחלט של גוף האתר */
    .main-wrapper {{
        margin-top: 100px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        width: 100%;
        direction: rtl;
    }}

    .hero-container {{
        max-width: 800px;
        margin: 0 auto;
    }}

    .hero-title {{
        color: {deep_blue};
        font-size: 3.8rem !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }}

    .hero-subtitle {{
        color: #64748B;
        font-size: 1.5rem !important;
        margin-bottom: 40px !important;
    }}

    /* עיצוב כפתור ההפעלה - גרדיאנט טורקיז/סגול */
    .stButton>button {{
        background: linear-gradient(90deg, #6366F1 0%, #34D399 100%) !important;
        color: white !important;
        border: none !important;
        padding: 16px 80px !important;
        border-radius: 50px !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        box-shadow: 0 10px 20px rgba(99, 102, 241, 0.3) !important;
        transition: 0.3s;
    }}

    /* מירכוז העמודות של העלאת הקבצים */
    [data-testid="stHorizontalBlock"] {{
        justify-content: center !important;
        gap: 20px !important;
    }}

    /* הסרת מסגרות מיותרות מהלוגו */
    .header-logo-img {{
        height: 55px;
        width: auto;
    }}
    </style>

    <div class="custom-header">
        <div style="color: white; display: flex; gap: 25px; font-weight: 500;">
            <span>אודות</span>
            <span>צור קשר</span>
            <span>בורר</span>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="color: white; font-size: 1.8rem; font-weight: bold;">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="header-logo-img">
        </div>
    </div>
    """, unsafe_allow_html=True)

# גוף האתר - הכל בתוך wrapper למירכוז
st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="hero-container">', unsafe_allow_html=True)

st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # סגירת hero-container

# יצירת העמודות
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📝 צד א' - תובע")
    file1 = st.file_uploader("גרור לכאן כתב תביעה", key="tov_file")

with col2:
    st.markdown("### 🛡️ צד ב' - נתבע")
    file2 = st.file_uploader("גרור לכאן כתב הגנה", key="nit_file")

st.markdown("<br><br>", unsafe_allow_html=True)

# כפתור הפעלה
if st.button("קבל הכרעת בורר עכשיו"):
    if file1 and file2:
        with st.spinner('מנתח את המסמכים המשפטיים...'):
            time.sleep(3)
        st.success("הניתוח הושלם!")
        st.balloons()
    else:
        st.warning("אנא העלה את שני המסמכים כדי שנוכל לבצע השוואה.")

st.markdown('</div>', unsafe_allow_html=True) # סגירת main-wrapper
