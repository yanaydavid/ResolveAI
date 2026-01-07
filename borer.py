import streamlit as st
import time

# הגדרות מותג
APP_NAME = "Resolve AI"
PRIMARY_COLOR = "#2563EB" 

st.set_page_config(page_title=APP_NAME, page_icon="⚖️", layout="centered")

# הגדרת כיוון כתיבה מימין לשמאל (RTL)
st.markdown("""
    <style>
    .main { text-align: right; direction: rtl; }
    div.stButton > button { width: 100%; }
    .stMarkdown, .stTextInput, .stFileUploader { text-align: right; direction: rtl; }
    </style>
""", unsafe_allow_html=True)

# עיצוב כותרת (Header)
st.markdown(f"""
    <div style='text-align: center; direction: rtl;'>
        <h1 style='color: {PRIMARY_COLOR}; font-size: 3rem;'>{APP_NAME}</h1>
        <p style='font-size: 1.2rem; color: #6B7280;'>פתרון סכסוכים חכם בבינה מלאכותית</p>
    </div>
    <hr style='border: 1px solid #E5E7EB;'>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: right;'>הגשת מסמכים לבוררות</h3>", unsafe_allow_html=True)

# מבנה טפסים - צד ימין ושמאל הפוכים כדי שייראה נכון בעברית
col1, col2 = st.columns(2)

with col2: # צד ימין במסך
    st.markdown("**צד א' (תובע)**")
    side_a = st.text_input("שם מלא", key="name_a", placeholder="הכנס שם...")
    file_a = st.file_uploader("כתב תביעה / חוזה (PDF)", type="pdf", key="file_a")
    
with col1: # צד שמאל במסך
    st.markdown("**צד ב' (נתבע)**")
    side_b = st.text_input("שם מלא", key="name_b", placeholder="הכנס שם...")
    file_b = st.file_uploader("כתב הגנה / נספחים (PDF)", type="pdf", key="file_b")

st.markdown("<br>", unsafe_allow_html=True)

# כפתור הפעלה
if st.button(f"הפעל את מערכת {APP_NAME}"):
    if file_a and file_b and side_a and side_b:
        with st.status("מנתח מסמכים משפטיים...", expanded=True) as status:
            time.sleep(1.5)
            st.write(f"סורק את הטענות של {side_a}...")
            time.sleep(1.5)
            st.write(f"מצליב נתונים מול כתב ההגנה של {side_b}...")
            status.update(label="הניתוח הסתיים בהצלחה!", state="complete", expanded=False)
        
        st.success("פסק בוררות מוכן!")
        
        with st.expander("לחץ כאן לצפייה בהחלטה המלאה", expanded=True):
            st.markdown(f"""
            <div style='text-align: right; direction: rtl;'>
            <h3>סיכום Resolve AI:</h3>
            <p><b>נושא הסכסוך:</b> אי-עמידה בלוחות זמנים של חוזה שירות.</p>
            <p><b>ממצאים:</b> נמצא כי {side_b} חרג מהמועד ב-14 ימי עסקים ללא הודעה מראש.</p>
            <p><b>החלטה:</b> פיצוי מוסכם בסך <b>1,500 ש"ח</b> לטובת {side_a}.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("נא למלא את כל השדות ולהעלות את המסמכים הנדרשים.")

st.markdown("<br><hr><p style='text-align: center; color: #9CA3AF;'>© 2024 Resolve AI - טכנולוגיה ליישוב סכסוכים</p>", unsafe_allow_html=True)
