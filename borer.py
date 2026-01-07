import streamlit as st
import time

# הגדרות דף
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# עיצוב CSS סופי ומדויק
st.markdown("""
    <style>
    /* הסתרת Header מובנה */
    [data-testid="stHeader"] {display: none !important;}
    .block-container {padding: 0 !important;}

    /* ה-Header הכחול - מתיחה מלאה */
    .nav-bar {
        background-color: #0A2647;
        width: 100vw;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 60px;
        position: relative;
        box-sizing: border-box;
    }

    /* תיקון הלוגו: שימוש ב-mask להסרת הרקע הלבן לגמרי */
    .logo-frame {
        height: 55px;
        width: 55px;
        background-color: white;
        mask: url(https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png) no-repeat center;
        mask-size: contain;
        -webkit-mask: url(https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png) no-repeat center;
        -webkit-mask-size: contain;
    }

    .main-container {
        text-align: center;
        padding: 60px 10%;
        background-color: #F8FAFC;
        min-height: 100vh;
        direction: rtl;
    }

    .hero-title {
        color: #0A2647;
        font-size: 4rem;
        font-weight: 900;
        margin: 0;
        display: block;
        width: 100%;
    }

    .hero-subtitle {
        color: #64748B;
        font-size: 1.5rem;
        margin-bottom: 40px;
        display: block;
        width: 100%;
    }

    /* עיצוב כפתור הטורקיז */
    .stButton > button {
        background: linear-gradient(90deg, #1E3A8A, #34D399) !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 80px !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(52, 211, 153, 0.2) !important;
    }
    
    /* מירכוז כותרות בתוך עמודות */
    h3 { text-align: center !important; color: #0A2647; }
    </style>
    
    <div class="nav-bar">
        <div style="color: white; font-weight: 500; display: flex; gap: 20px;">
            <span>אודות</span>
            <span>צור קשר</span>
        </div>
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="color: white; font-size: 1.8rem; font-weight: bold;">Resolve AI</span>
            <div class="logo-frame"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# גוף האתר
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">פתרון סכסוכים חכם ומהיר מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

# עמודות להעלאת קבצים
col1, space, col2 = st.columns([1, 0.1, 1])

with col1:
    st.markdown("### 📝 צד א' - תובע")
    file1 = st.file_uploader("העלה כתב תביעה", key="t1")

with col2:
    st.markdown("### 🛡️ צד ב' - נתבע")
    file2 = st.file_uploader("העלה כתב הגנה", key="n1")

st.markdown("<br>", unsafe_allow_html=True)

# לוגיקה אמיתית (בסיסית) להפעלת התהליך
if st.button("התחל תהליך בוררות"):
    if file1 and file2:
        with st.spinner('הבינה המלאכותית מנתחת את המסמכים ומשווה טענות...'):
            # כאן יבוא בעתיד החיבור ל-LLM
            time.sleep(4)
        
        st.success("הניתוח הושלם!")
        
        # הדמיית תוצאה
        st.markdown("---")
        st.subheader("טיוטת פסק בורר (הדמיה)")
        st.info(f"""
        **מסקנה ראשונית:** לאחר ניתוח כתב התביעה ({file1.name}) וכתב ההגנה ({file2.name}), 
        נמצא כי ישנה סתירה מהותית בסעיף האחריות החוזית. 
        **המלצה:** פשרה בגובה 65% מהסכום הנתבע.
        """)
    else:
        st.error("אנא וודא שהעלית מסמכים משני הצדדים לפני הלחיצה.")

st.markdown('</div>', unsafe_allow_html=True)
