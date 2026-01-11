import streamlit as st
import os
from database import create_case, get_case, update_case_status

# Create uploads directory if it doesn't exist
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Initialize session state
if 'case_id' not in st.session_state:
    st.session_state.case_id = None
if 'show_delivery' not in st.session_state:
    st.session_state.show_delivery = False

# Page configuration
st.set_page_config(
    page_title="Resolve AI - בוררות דיגיטלית",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');

    * {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
    }

    /* Hide Streamlit default elements */
    header[data-testid="stHeader"],
    footer {
        visibility: hidden;
        height: 0;
    }

    .block-container {
        padding-top: 0 !important;
        max-width: 100% !important;
    }

    /* Background */
    [data-testid="stAppViewContainer"] {
        background: #F1F5F9;
    }

    /* Custom Header - Sticky */
    .custom-header {
        background: #0A2647;
        height: 100px;
        position: sticky;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 5%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Logo */
    .logo {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .logo img {
        height: 60px;
        width: 60px;
        border-radius: 50%;
    }

    .logo-text {
        color: white;
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .logo-ai {
        background: linear-gradient(135deg, #7C3AED, #6366F1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Navigation */
    .nav-menu {
        display: flex;
        gap: 30px;
        align-items: center;
    }

    .nav-item {
        color: white;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
        cursor: pointer;
        text-decoration: none;
    }

    .nav-item:hover {
        background: rgba(255,255,255,0.1);
        transform: translateY(-2px);
    }

    .nav-item.active {
        background: linear-gradient(135deg, #7C3AED, #6366F1);
    }

    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 80px 10% 60px;
        background: linear-gradient(135deg, #F1F5F9 0%, #E0E7FF 100%);
    }

    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #7C3AED, #6366F1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        letter-spacing: -2px;
    }

    .hero-subtitle {
        font-size: 1.8rem;
        color: #475569;
        font-weight: 500;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* Main Content */
    .main-content {
        padding: 60px 10%;
        max-width: 1400px;
        margin: 0 auto;
    }

    /* Card */
    .card {
        background: white;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.08);
        margin-bottom: 30px;
        transition: all 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(0,0,0,0.12);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #7C3AED, #6366F1) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 15px 40px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.4) !important;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .custom-header {
            flex-direction: column;
            height: auto;
            padding: 20px;
        }

        .nav-menu {
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
        }

        .hero-title {
            font-size: 3rem;
        }

        .hero-subtitle {
            font-size: 1.3rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header with Navigation
st.markdown("""
    <div class="custom-header">
        <div class="logo">
            <img src="https://raw.githubusercontent.com/yanaydavid/ResolveAI/main/logo.png" alt="Resolve AI">
            <div class="logo-text">Resolve <span class="logo-ai">AI</span></div>
        </div>
        <div class="nav-menu">
            <div class="nav-item active">בורר</div>
            <div class="nav-item">חיפוש תיק</div>
            <div class="nav-item">שירותים</div>
            <div class="nav-item">אודות</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Resolve AI</h1>
        <p class="hero-subtitle">
            פתרון בוררות דיגיטלי מבוסס בינה מלאכותית -
            מהפכה בעולם יישוב סכסוכים משפטיים
        </p>
    </div>
""", unsafe_allow_html=True)

# Main Content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Claimant Portal
st.markdown("""
    <div class="card">
        <h2 style='color: #0A2647; font-size: 2.5rem; margin-bottom: 10px; text-align: center;'>
            🏛️ פורטל תובעים
        </h2>
        <p style='font-size: 1.2rem; color: #64748B; text-align: center; margin-bottom: 30px;'>
            הגש את כתב התביעה שלך ותקבל מספר תיק ייחודי
        </p>
    </div>
""", unsafe_allow_html=True)

# File Upload Section
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
    <h3 style='color: #0A2647; font-size: 1.8rem; margin-bottom: 20px;'>
        📄 העלאת כתב תביעה
    </h3>
""", unsafe_allow_html=True)

# Input for claimant name
claimant_name = st.text_input(
    "שם התובע המלא",
    placeholder="הכנס את שמך המלא...",
    help="הכנס את השם המלא של התובע"
)

# File uploader
uploaded_file = st.file_uploader(
    "העלה כתב תביעה (PDF)",
    type=["pdf"],
    help="העלה את כתב התביעה שלך בפורמט PDF"
)

# Check if we should show delivery screen
if not st.session_state.show_delivery:
    # Submit button
    if st.button("🚀 הגש תביעה"):
        if not claimant_name:
            st.error("⚠️ נא להזין את שם התובע")
        elif not uploaded_file:
            st.error("⚠️ נא להעלות קובץ כתב תביעה")
        else:
            # Save the uploaded file
            file_path = os.path.join("uploads", f"{claimant_name}_{uploaded_file.name}")
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Create case in database with mailing cost
            case_id = create_case(
                claimant_name=claimant_name,
                claim_file_path=file_path,
                mailing_cost=35.0
            )

            # Save to session state and show delivery screen
            st.session_state.case_id = case_id
            st.session_state.claimant_name = claimant_name
            st.session_state.show_delivery = True
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Delivery & Payment Section
if st.session_state.show_delivery and st.session_state.case_id:
    st.markdown("""
        <div class="card">
            <h2 style='color: #0A2647; font-size: 2.5rem; margin-bottom: 10px; text-align: center;'>
                📬 סיכום ומשלוח
            </h2>
            <p style='font-size: 1.2rem; color: #64748B; text-align: center; margin-bottom: 30px;'>
                התיק נוצר בהצלחה! עכשיו נשלח את התביעה לנתבע
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Case ID Display
    st.markdown(f"""
        <div style='background: linear-gradient(135deg, #7C3AED, #6366F1); padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 30px;'>
            <h3 style='color: white; font-size: 1.3rem; margin-bottom: 10px;'>מספר תיק שלך</h3>
            <h1 style='color: white; font-size: 3.5rem; font-weight: 900; margin: 0;'>{st.session_state.case_id}</h1>
            <p style='color: rgba(255,255,255,0.9); margin-top: 10px; font-size: 1.1rem;'>שמור מספר זה למעקב אחר התיק</p>
        </div>
    """, unsafe_allow_html=True)

    # Delivery Information
    st.markdown("""
        <div style='background: #FEF3C7; padding: 20px; border-radius: 12px; border-right: 4px solid #F59E0B; margin-bottom: 25px;'>
            <h4 style='color: #92400E; font-size: 1.4rem; margin-bottom: 10px;'>⚠️ שלב חובה: משלוח התביעה לנתבע</h4>
            <p style='color: #78350F; font-size: 1.1rem; line-height: 1.7;'>
                כדי להמשיך בהליך הבוררות, <b>יש לשלוח את התביעה בדואר רשום לנתבע</b>.
                <br>זהו תהליך משפטי חובה המבטיח שהנתבע קיבל את כתב התביעה באופן רשמי.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Delivery Option
    st.markdown("""
        <div style='background: white; padding: 25px; border-radius: 15px; border: 2px solid #7C3AED; margin-bottom: 25px;'>
            <div style='display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;'>
                <div>
                    <h4 style='color: #0A2647; font-size: 1.5rem; margin: 0;'>📮 דואר רשום באמצעות Resolve AI</h4>
                    <p style='color: #64748B; font-size: 1.1rem; margin-top: 8px;'>
                        אנחנו נדאג לשלוח את התביעה בדואר רשום ישירות לנתבע
                    </p>
                </div>
                <div style='text-align: left;'>
                    <div style='font-size: 2.5rem; font-weight: 800; color: #7C3AED;'>35 ₪</div>
                </div>
            </div>
            <div style='background: #F1F5F9; padding: 15px; border-radius: 10px;'>
                <p style='color: #475569; font-size: 1rem; margin: 0;'>
                    💡 <b>חשוב לדעת:</b> עלות זו תתווסף אוטומטית להוצאות המשפט בפסק הדין הסופי,
                    ותוחזר לך במקרה של ניצחון בתיק.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Summary
    st.markdown("""
        <div style='background: #F8FAFC; padding: 20px; border-radius: 12px; margin-bottom: 25px;'>
            <h4 style='color: #0A2647; font-size: 1.3rem; margin-bottom: 15px;'>💰 סיכום עלויות</h4>
            <div style='display: flex; justify-content: space-between; font-size: 1.2rem; color: #475569; margin-bottom: 10px;'>
                <span>דמי משלוח בדואר רשום</span>
                <span style='font-weight: 600;'>35 ₪</span>
            </div>
            <hr style='border: none; border-top: 2px solid #E2E8F0; margin: 15px 0;'>
            <div style='display: flex; justify-content: space-between; font-size: 1.5rem; font-weight: 700; color: #0A2647;'>
                <span>סה"כ לתשלום</span>
                <span style='color: #7C3AED;'>35 ₪</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Confirm & Pay Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ אשר ושלם", use_container_width=True):
            # Update case status to 'Sent'
            update_case_status(st.session_state.case_id, "Sent")

            st.success("""
                ✅ התשלום אושר והתביעה נשלחת!

                התיק עודכן לסטטוס "נשלח".
                נעדכן אותך כשהנתבע יקבל את התביעה.
            """)
            st.balloons()

            # Show final summary
            st.info(f"""
                📋 **סיכום סופי:**
                - מספר תיק: **{st.session_state.case_id}**
                - שם התובע: {st.session_state.claimant_name}
                - סטטוס: נשלח בדואר רשום
                - עלות משלוח: 35 ₪ (תתווסף להוצאות המשפט)

                תוכל לעקוב אחר התיק באמצעות מספר התיק שלך.
            """)

            # Clear session state after confirmation
            if st.button("🏠 חזור לדף הבית"):
                st.session_state.case_id = None
                st.session_state.show_delivery = False
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
