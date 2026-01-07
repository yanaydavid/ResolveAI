import streamlit as st
import time

# הגדרות דף
st.set_page_config(page_title="Resolve AI", page_icon="⚖️", layout="wide")

# עיצוב CSS למיתוג (כחול עמוק וטורקיז)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; direction: rtl; }
    .main-title { color: #1e3a8a; font-family: 'Assistant', sans-serif; text-align: center; font-size: 3rem; margin-top: -20px; }
    .sub-title { color: #64748b; text-align: center; font-size: 1.2rem; margin-bottom: 2rem; }
    .stButton>button { width: 100%; background-color: #06b6d4 !important; color: white !important; border-radius: 12px; padding: 15px; font-weight: bold; border: none; }
    .stButton>button:hover { background-color: #0891b2 !important; }
    </style>
    """, unsafe_allow_html=True)

# הצגת הלוגו שהעלית במרכז
col_l1, col_l2, col_l3 = st.columns([2, 1, 2])
with col_l2:
    st.image("logo.png", use_container_width=True)

# כותרות
st.markdown('<h1 class="main-title">Resolve AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">יישוב סכסוכים חכם מבוסס בינה מלאכותית</p>', unsafe_allow_html=True)

st.divider()

# ממשק העלאת מסמכים
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📝 צד א' (התובע)")
    tovea = st.file_uploader("העלה כתב תביעה", key="t1")
with col2:
    st.markdown("### 🛡️ צד ב' (הנתבע)")
    nitba = st.file_uploader("העלה כתב הגנה", key="n1")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("קבל הכרעת בורר עכשיו"):
    if tovea and nitba:
        with st.spinner('מנתח מסמכים בעזרת AI...'):
            time.sleep(3)
        st.success("הניתוח הושלם!")
        st.markdown("""
            <div style="background-color: white; padding: 30px; border-radius: 15px; border-right: 5px solid #06b6d4; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <h2 style="color: #1e3a8a;">פסק דין סופי</h2>
                <p>מערכת Resolve AI ניתחה את הטענות ומצאה כי יש לקבל את התביעה בחלקה...</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("נא להעלות מסמכים משני הצדדים.")
