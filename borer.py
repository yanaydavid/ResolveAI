import streamlit as st
import time

# הגדרות דף
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# עיצוב CSS מתקדם להצמדת הלוגו לשמאל בתוך פס כחול
st.markdown("""
    <style>
    /* ניקוי רווחים מיותרים למעלה */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }
    
    /* יצירת פס כחול עליון (Navbar) */
    .nav-bar {
        background-color: #1a3a5a; /* הכחול העמוק מהדוגמה */
        padding: 15px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        margin-bottom: 40px;
        width: 100%;
    }
    
    .nav-logo-container {
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .nav-links {
        display: flex;
        gap: 25px;
        font-family: 'Assistant', sans-serif;
    }

    /* עיצוב כותרות וטקסט בעברית */
    body, .main {
        direction: rtl;
        text-align: right;
        background-color: #f4f7f9;
    }
    
    .main-header {
        color: #1a3a5a;
        font-weight: bold;
        text-align: center;
        font-size: 2.5rem;
    }
    
    .sub-header {
        color: #555;
        text-align: center;
        margin-bottom: 40px;
    }

    /* עיצוב כפתור הכרעה */
    .stButton>button {
        background-color: #1a3a5a !important;
        color: white !important;
        border-radius: 8px;
        padding: 10px 30px;
        font-weight: bold;
        width: auto;
        display: block;
        margin: 0 auto;
    }
    </style>
    """, unsafe_allow_html=True)

# בניית ה-Navbar (הפס הכחול למעלה)
# כאן אנחנו משתמשים ב-HTML כדי להכניס את הלוגו לצד שמאל של הפס
st.markdown(f"""
    <div class="nav-bar">
        <div class="nav-links">
            <span>אודות</span>
            <span>שירותים</span>
            <span>צור קשר</span>
        </div>
        <div class="nav-logo-container">
            <span style="font-size: 20px; font-weight: bold;">Resolve AI</span>
            <img src="https://raw.githubusercontent.com/{st.context.user_id if 'user_id' in dir(st.context) else 'yanaydavid'}/ResolveAI/main/logo.png" width="40">
        </div>
    </div>
    """, unsafe_allow_html=True)

# תוכן האתר
st.markdown('<h1 class="main-header">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">מערכת בינה מלאכותית ליישוב סכסוכים והכרעות בוררות</p>', unsafe_allow_html=True)

# ממשק העלאת מסמכים בתוך "כרטיסים" לבנים
col1, col2 = st.columns(2)

with col1:
    st.info("### 📝 צד א' - תובע")
    tovea = st.file_uploader("העלה כתב תביעה או חוזה", key="tovea_up")

with col2:
    st.info("### 🛡️ צד ב' - נתבע")
    nitba = st.file_uploader("העלה כתב הגנה או תגובה", key="nitba_up")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("קבל הכרעת בורר עכשיו"):
    if tovea and nitba:
        with st.spinner('מנתח מסמכים ומשווה טענות...'):
            time.sleep(3)
        st.success("הניתוח הושלם!")
        st.write("---")
        st.subheader("פסק בוררות מוצע:")
        st.write("לאחר בחינת המסמכים, נראה כי ישנה הפרה של סעיף 4 לחוזה...")
    else:
        st.warning("אנא העלה את המסמכים משני הצדדים לצורך הניתוח.")
