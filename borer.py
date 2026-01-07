import streamlit as st
import time
import base64

# הגדרות דף
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# פונקציה להמרת התמונה המקומית לפורמט שהדפדפן מציג בקלות
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

try:
    img_base64 = get_base64_of_bin_file('logo.png')
except:
    img_base64 = ""

# עיצוב CSS מתקדם - העתקה מדויקת של הסקיצה
st.markdown(f"""
    <style>
    /* הסתרת אלמנטים מיותרים של Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .block-container {{
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }}
    
    /* הפס הכחול העליון (Navbar) */
    .nav-bar {{
        background-color: #1a3a5a;
        padding: 10px 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        width: 100%;
        height: 70px;
    }}
    
    .nav-logo-section {{
        display: flex;
        align-items: center;
        gap: 12px;
        flex-direction: row-reverse; /* לוגו משמאל לטקסט */
    }}
    
    .nav-links {{
        display: flex;
        gap: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    /* גוף הדף */
    .content-area {{
        padding: 40px 10%;
        direction: rtl;
        text-align: center;
        background-color: #f4f7f9;
        min-height: 100vh;
    }}
    
    .main-header {{
        color: #1a3a5a;
        font-size: 2.8rem;
        margin-bottom: 10px;
    }}
    
    .card {{
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    </style>
    
    <div class="nav-bar">
        <div class="nav-links">
            <span>אודות</span>
            <span>שאלות נפוצות</span>
            <span>צור קשר</span>
        </div>
        <div class="nav-logo-section">
            <span style="font-size: 22px; font-weight: bold; letter-spacing: 1px;">Resolve AI</span>
            <img src="data:image/png;base64,{img_base64}" width="45">
        </div>
    </div>
    """, unsafe_allow_html=True)

# תוכן האתר בתוך הקונטיינר המעוצב
st.markdown('<div class="content-area">', unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #666; font-size: 1.2rem;">הליך בוררות חכם, מהיר והוגן מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# עמודות להעלאת קבצים
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📝 צד א' - תובע")
    st.file_uploader("העלה כתב תביעה / מסמכים", key="t1")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🛡️ צד ב' - נתבע")
    st.file_uploader("העלה כתב הגנה / תגובה", key="n1")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("בצע הכרעה עכשיו"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם! ניתן להוריד את טיוטת פסק הבורר.")

st.markdown('</div>', unsafe_allow_html=True)
