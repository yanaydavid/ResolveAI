import streamlit as st
import time

# הגדרות דף
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# הצבעים שביקשת
color_blue = "#2563EB"    # כחול עמוק
color_grey = "#6B7280"    # אפור כסוף
color_turquoise = "#34D399" # טורקיז/ירוק בהיר

# עיצוב CSS מותאם אישית (אפשרות 1 - הייטק מינימליסטי)
st.markdown(f"""
    <style>
    /* הסתרת כותרות ברירת מחדל */
    header {{visibility: hidden;}}
    .block-container {{padding-top: 0px;}}

    /* פס עליון */
    .nav-bar {{
        background-color: {color_blue};
        padding: 10px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        height: 70px;
        margin-bottom: 50px;
    }}
    
    /* גוף האתר */
    .main-body {{
        direction: rtl;
        text-align: center;
        font-family: 'Assistant', sans-serif;
    }}
    
    .title-text {{
        color: {color_blue};
        font-weight: 800;
        font-size: 3rem;
        margin-bottom: 5px;
    }}
    
    .subtitle-text {{
        color: {color_grey};
        font-size: 1.2rem;
        margin-bottom: 40px;
    }}

    /* כרטיסי העלאה */
    .stFileUploader {{
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 10px;
        background-color: white;
    }}

    /* כפתור טורקיז */
    .stButton>button {{
        background-color: {color_turquoise} !important;
        color: #1f2937 !important;
        font-weight: bold !important;
        border: none !important;
        padding: 15px 50px !important;
        border-radius: 8px !important;
        font-size: 1.1rem !important;
        transition: 0.3s;
    }}
    
    .stButton>button:hover {{
        opacity: 0.9;
        transform: scale(1.02);
    }}
    </style>
    
    <div class="nav-bar">
        <div style="display: flex; gap: 20px;">
            <span>אודות</span>
            <span>צור קשר</span>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="font-weight: bold; font-size: 1.2rem;">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" width="40">
        </div>
    </div>
    """, unsafe_allow_html=True)

# תוכן האתר
st.markdown('<div class="main-body">', unsafe_allow_html=True)
st.markdown('<h1 class="title-text">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# אזור העלאת קבצים
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown(f"<h3 style='color: {color_blue};'>📝 צד א' - תובע</h3>", unsafe_allow_html=True)
    st.file_uploader("העלה כתב תביעה", key="up1")

with col2:
    st.markdown(f"<h3 style='color: {color_blue};'>🛡️ צד ב' - נתבע</h3>", unsafe_allow_html=True)
    st.file_uploader("העלה כתב הגנה", key="up2")

st.markdown("<br><br>", unsafe_allow_html=True)

# כפתור הפעלה
if st.button("התחל ניתוח ובוררות"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.balloons()
    st.success("הניתוח הסתיים! ניתן לצפות בטיוטת פסק הבורר.")

st.markdown('</div>', unsafe_allow_html=True)
