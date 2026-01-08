import streamlit as st
import time

# הגדרות דף - Resolve AI Platform
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# אתחול session state לכפתור אודות
if 'show_about' not in st.session_state:
    st.session_state.show_about = False

# ערכת צבעים מדויקת לפי התמונה
primary_blue = "#1a4d5e"  # כחול כהה ל-header
secondary_blue = "#2a5f73"  # כחול בינוני לגרדיאנט
accent_cyan = "#00d4ff"  # ציאן בהיר ל-AI
bg_light = "#e8ecf0"  # רקע בהיר אפרפר
card_bg = "#ffffff"  # לבן לכרטיסים

# CSS מעוצב ומותאם לעברית
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');

    * {{
        font-family: 'Heebo', sans-serif;
        box-sizing: border-box;
    }}

    /* הסתרת אלמנטים של Streamlit */
    header, [data-testid="stHeader"], footer {{
        visibility: hidden !important;
        height: 0 !important;
        display: none !important;
    }}

    .block-container {{
        padding: 0px !important;
        max-width: 100% !important;
    }}

    [data-testid="stAppViewContainer"] {{
        background: {bg_light} !important;
    }}

    /* מניעת מלבנים לבנים בתצוגות שונות */
    .main, [data-testid="stApp"], body {{
        background-color: {bg_light} !important;
    }}

    /* Header מעוצב בכחול כהה */
    .custom-header {{
        background: linear-gradient(135deg, {primary_blue} 0%, {secondary_blue} 100%);
        height: 95px;
        display: flex;
        align-items: center;
        padding: 0 60px;
        justify-content: space-between;
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9999;
        box-shadow: 0 2px 15px rgba(0,0,0,0.1);
    }}

    .logo-section {{
        display: flex;
        align-items: center;
        gap: 15px;
        direction: ltr;
    }}

    .logo-img {{
        height: 70px;
        width: 70px;
        border-radius: 50%;
    }}

    .logo-text {{
        color: white;
        font-size: 1.9rem;
        font-weight: 700;
    }}

    .logo-ai {{
        color: {accent_cyan};
    }}

    /* חלון אודות */
    .about-modal {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        max-width: 700px;
        width: 90%;
        z-index: 10000;
        direction: rtl;
        text-align: right;
        max-height: 80vh;
        overflow-y: auto;
    }}

    .about-overlay {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0,0,0,0.6);
        z-index: 9999;
    }}

    .about-close {{
        position: absolute;
        top: 20px;
        left: 20px;
        background: {accent_cyan};
        color: white;
        border: none;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        font-size: 1.3rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }}

    .about-close:hover {{
        background: {primary_blue};
        transform: rotate(90deg);
    }}

    .about-title {{
        color: {primary_blue};
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 30px;
        text-align: center;
    }}

    .about-subtitle {{
        color: {accent_cyan};
        font-size: 1.5rem;
        font-weight: 700;
        margin: 25px 0 15px 0;
    }}

    .about-text {{
        color: #334155;
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 15px;
    }}

    /* גוף האתר - ממורכז לחלוטין, ללא שטח מת */
    .main-content {{
        margin-top: 100px;
        text-align: center;
        direction: rtl;
        padding: 15px 10%;
        background: {bg_light};
        min-height: calc(100vh - 100px);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* כותרת ראשית - בצבע טורקיז */
    .hero-title {{
        color: {accent_cyan};
        font-size: 3.8rem;
        font-weight: 900;
        margin: 0 auto 10px auto;
        text-align: center;
        width: 100%;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}

    /* כותרת משנה - ממורכזת */
    .hero-subtitle {{
        font-size: 1.35rem;
        color: #64748B;
        margin: 0 auto 40px auto;
        text-align: center;
        width: 100%;
    }}

    /* כרטיסים מעוצבים */
    .card {{
        background: {card_bg};
        border-radius: 20px;
        padding: 45px 35px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }}

    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 35px rgba(0,0,0,0.15);
    }}

    /* כותרת בכרטיס - ממורכזת ובצבע header */
    .card-title {{
        color: {primary_blue};
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 15px;
        text-align: center;
        width: 100%;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }}

    /* כותרת משנה בכרטיס - ממורכזת */
    .card-subtitle {{
        color: #94a3b8;
        font-size: 1.15rem;
        margin-bottom: 30px;
        text-align: center;
        width: 100%;
    }}

    .card-button {{
        background: {primary_blue};
        color: white;
        padding: 13px 45px;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }}

    .card-button:hover {{
        background: {secondary_blue};
        transform: scale(1.05);
    }}

    /* מירכוז עמודות Streamlit */
    [data-testid="column"] {{
        display: flex;
        justify-content: center;
    }}

    /* כפתור מרכזי עם גרדיאנט סגול - ממורכז לגמרי */
    .stButton {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        text-align: center !important;
    }}

    .stButton>button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #667eea 100%) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 20px 90px !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        border: none !important;
        margin: 40px auto !important;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        animation: gradient 3s ease infinite !important;
        display: block !important;
    }}

    .stButton>button:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.6) !important;
    }}

    @keyframes gradient {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    /* הסתרת אלמנטי העלאה של Streamlit */
    .stFileUploader {{
        display: none;
    }}

    /* כפתור אודות בצד ימין ב-header */
    div[data-testid="column"]:has(.about-btn-container) {{
        position: fixed !important;
        top: 27px !important;
        right: 60px !important;
        z-index: 10000 !important;
        width: auto !important;
    }}

    .about-btn-container .stButton>button {{
        background: rgba(255,255,255,0.1) !important;
        border: 2px solid {accent_cyan} !important;
        padding: 10px 30px !important;
        border-radius: 25px !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        margin: 0 !important;
        animation: none !important;
        box-shadow: none !important;
    }}

    .about-btn-container .stButton>button:hover {{
        background: {accent_cyan} !important;
        color: {primary_blue} !important;
        transform: scale(1.05) !important;
        box-shadow: none !important;
    }}

    /* התאמה למסכים קטנים */
    @media (max-width: 768px) {{
        .custom-header {{
            padding: 0 20px;
        }}

        .hero-title {{
            font-size: 2.5rem;
        }}

        div[data-testid="column"]:has(.about-btn-container) {{
            right: 20px !important;
        }}
    }}
    </style>

    <div class="custom-header">
        <div class="logo-section">
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" class="logo-img">
            <div class="logo-text">Resolve <span class="logo-ai">AI</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# כפתור אודות בעמודה מיוחדת (יוצב ב-header ע"י CSS)
col_about = st.columns([1])[0]
with col_about:
    st.markdown('<div class="about-btn-container">', unsafe_allow_html=True)
    if st.button("אודות"):
        st.session_state.show_about = True
    st.markdown('</div>', unsafe_allow_html=True)

# הצגת חלון אודות
if st.session_state.show_about:
    st.markdown("""
    <div class="about-overlay"></div>
    <div class="about-modal">
        <h1 class="about-title">Resolve AI - בוררות מבוססת בינה מלאכותית</h1>

        <h2 class="about-subtitle">מהפכה דיגיטלית בעולם יישוב הסכסוכים</h2>
        <p class="about-text">
            Resolve AI מציעה פתרון חדשני ומתקדם ליישוב סכסוכים משפטיים באמצעות טכנולוגיית בינה מלאכותית מתקדמת.
            המערכת שלנו נועדה לספק החלטות בוררות מקצועיות, אובייקטיביות ומהירות, תוך חיסכון משמעותי בזמן ובעלויות.
        </p>

        <h2 class="about-subtitle">היתרונות המשמעותיים</h2>
        <p class="about-text">
            <strong>חיסכון כלכלי משמעותי:</strong> במקום לשלם אלפי שקלים לעורכי דין ובעלי מקצוע משפטיים, תקבלו החלטת בוררות מקצועית בשבריר מהעלות המקובלת.
        </p>
        <p class="about-text">
            <strong>מהירות וזמינות:</strong> תהליך הבוררות המסורתי עלול להימשך חודשים ואף שנים. עם Resolve AI, תקבלו החלטה מנומקת תוך דקות בודדות, בכל שעה ומכל מקום.
        </p>
        <p class="about-text">
            <strong>אובייקטיביות מלאה:</strong> הבינה המלאכותית שלנו מנתחת את המקרה ללא משוא פנים, ללא דעות קדומות וללא השפעות חיצוניות, תוך הסתמכות על פסיקה משפטית עדכנית ועקרונות משפט מבוססים.
        </p>

        <h2 class="about-subtitle">איך זה עובד?</h2>
        <p class="about-text">
            1. <strong>העלאת מסמכים:</strong> הצד התובע מעלה את כתב התביעה, והצד הנתבע מעלה את כתב ההגנה.<br>
            2. <strong>ניתוח חכם:</strong> המערכת שלנו מנתחת את שני הצדדים, בוחנת את הטיעונים, בוחנת תקדימים משפטיים רלוונטיים ואת החקיקה הרלוונטית.<br>
            3. <strong>החלטת בוררות:</strong> תקבלו החלטה מפורטת ומנומקת המבוססת על עקרונות משפטיים מוכחים, עם הפניות לפסיקה ולחקיקה.
        </p>

        <h2 class="about-subtitle">למי זה מתאים?</h2>
        <p class="about-text">
            המערכת שלנו מתאימה לסכסוכים אזרחיים, מסחריים, צרכניים ועוד. בין אם מדובר בסכסוך בין שכנים, בין עסקים,
            או בין צרכן לספק - Resolve AI כאן כדי לספק לכם פתרון מהיר, זול ואפקטיבי.
        </p>

        <p class="about-text" style="text-align:center; margin-top:30px; font-weight:600; color:#00d4ff;">
            הצטרפו למהפכה הדיגיטלית ביישוב סכסוכים - פשוט, מהיר וחסכוני.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # כפתור סגירה
    if st.button("✕ סגור", key="close_about"):
        st.session_state.show_about = False
        st.rerun()

# גוף האתר
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# כותרת ראשית וכותרת משנה - ממורכזות
st.markdown('<h1 class="hero-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">תיווך בינה מלאכותית לפתרון סכסוכים מהיר ואובייקטיבי</p>', unsafe_allow_html=True)

# כרטיסים - ממורכזים
col1, space, col2 = st.columns([1, 0.15, 1])

with col1:
    st.markdown("""
    <div class="card">
        <h2 class="card-title">צד תובע</h2>
        <p class="card-subtitle">הגש תביעה משפטית</p>
        <button class="card-button">העלה כתב תביעה</button>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h2 class="card-title">צד נתבע</h2>
        <p class="card-subtitle">הגש הגנה משפטית</p>
        <button class="card-button">העלה כתב הגנה</button>
    </div>
    """, unsafe_allow_html=True)

# כפתור מרכזי עם גרדיאנט
if st.button("בצע בוררות כעת"):
    with st.spinner('מנתח מסמכים...'):
        time.sleep(2)
    st.success("הניתוח הושלם!")

st.markdown('</div>', unsafe_allow_html=True)
