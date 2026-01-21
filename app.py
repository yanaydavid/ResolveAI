import streamlit as st

# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="Resolve AI - בוררות דיגיטלית",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# Custom CSS - Luxury Design with RTL Support
# =====================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;900&display=swap');

    /* Global RTL Settings */
    * {
        font-family: 'Heebo', sans-serif;
        direction: rtl;
        text-align: right;
    }

    /* Hide Streamlit Branding */
    header[data-testid="stHeader"],
    footer,
    #MainMenu {
        visibility: hidden;
        height: 0;
    }

    .block-container {
        padding-top: 2rem !important;
        max-width: 100% !important;
    }

    /* Background - Deep Navy */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0A2647 0%, #144272 50%, #205295 100%);
        min-height: 100vh;
    }

    /* Main Content Container */
    .main-content {
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px;
    }

    /* Header Title */
    .main-title {
        color: white;
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 80px;
        margin-top: 40px;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }

    /* Portal Title */
    .portal-title {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 50px;
        margin-top: 20px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }

    /* Column Cards */
    .column-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 60px 40px;
        text-align: center;
        transition: all 0.4s ease;
        border: 2px solid transparent;
        backdrop-filter: blur(10px);
        min-height: 400px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .column-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.08);
        border: 2px solid rgba(218, 165, 32, 0.5);
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    }

    .column-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 40px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }

    /* Form Container */
    .form-container {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 50px;
        margin: 30px auto;
        max-width: 900px;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(218, 165, 32, 0.3);
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }

    .section-title {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    /* Luxury Buttons */
    .stButton > button {
        background: transparent !important;
        color: white !important;
        border: 3px solid #DAA520 !important;
        border-radius: 50px !important;
        padding: 20px 60px !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        transition: all 0.4s ease !important;
        box-shadow: 0 0 30px rgba(218, 165, 32, 0.3) !important;
        letter-spacing: 1px !important;
        width: 100% !important;
        max-width: 400px !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #DAA520, #FFD700) !important;
        color: #0A2647 !important;
        border-color: #FFD700 !important;
        box-shadow: 0 0 50px rgba(218, 165, 32, 0.6) !important;
        transform: scale(1.05) !important;
    }

    .stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Text Inputs */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(218, 165, 32, 0.4) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 15px 20px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #DAA520 !important;
        box-shadow: 0 0 20px rgba(218, 165, 32, 0.4) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }

    /* Labels */
    .stTextInput label {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    /* Checkbox */
    .stCheckbox {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 12px;
        border: 2px solid rgba(218, 165, 32, 0.3);
        margin: 30px 0;
    }

    .stCheckbox label {
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        line-height: 1.8 !important;
    }

    /* Warning/Info boxes */
    .stAlert {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 12px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* RTL Columns */
    [data-testid="column"] {
        direction: rtl;
        text-align: center;
    }

    /* Back Button Style */
    .back-button {
        margin-bottom: 30px;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
            margin-bottom: 40px;
        }

        .portal-title {
            font-size: 2rem;
        }

        .column-title {
            font-size: 1.8rem;
        }

        .column-card {
            padding: 40px 20px;
            min-height: 300px;
        }

        .form-container {
            padding: 30px 20px;
        }

        .stButton > button {
            font-size: 1.2rem !important;
            padding: 15px 40px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# =====================================================
# Initialize Session State
# =====================================================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'terms_accepted_claimant' not in st.session_state:
    st.session_state.terms_accepted_claimant = False
if 'terms_accepted_defendant' not in st.session_state:
    st.session_state.terms_accepted_defendant = False

# =====================================================
# Navigation Functions
# =====================================================
def go_to_claimant_portal():
    st.session_state.page = 'claimant_portal'

def go_to_defendant_portal():
    st.session_state.page = 'defendant_portal'

def go_to_home():
    st.session_state.page = 'home'
    st.session_state.terms_accepted_claimant = False
    st.session_state.terms_accepted_defendant = False

# =====================================================
# Page: Home (Landing Page)
# =====================================================
def render_home_page():
    # Main Title
    st.markdown("""
        <div class="main-content">
            <h1 class="main-title">ברוכים הבאים ל-Resolve AI</h1>
        </div>
    """, unsafe_allow_html=True)

    # Two Columns Layout
    col1, col2 = st.columns(2, gap="large")

    # Right Column - Claimant
    with col1:
        st.markdown("""
            <div class="column-card">
                <h2 class="column-title">רוצה להגיש תביעה?</h2>
            </div>
        """, unsafe_allow_html=True)

        if st.button("לחץ כאן", key="claimant_button"):
            go_to_claimant_portal()
            st.rerun()

    # Left Column - Defendant
    with col2:
        st.markdown("""
            <div class="column-card">
                <h2 class="column-title">רוצה להגיש כתב הגנה?</h2>
            </div>
        """, unsafe_allow_html=True)

        if st.button("לחץ כאן", key="defendant_button"):
            go_to_defendant_portal()
            st.rerun()

# =====================================================
# Page: Claimant Portal
# =====================================================
def render_claimant_portal():
    # Back Button
    st.markdown('<div class="back-button">', unsafe_allow_html=True)
    if st.button("חזרה לדף הבית", key="back_from_claimant"):
        go_to_home()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Portal Title
    st.markdown("""
        <h1 class="portal-title">מסוף תובעים</h1>
    """, unsafe_allow_html=True)

    # Form Container
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # Section Title
    st.markdown("""
        <h2 class="section-title">רישום תובע</h2>
    """, unsafe_allow_html=True)

    # Legal Agreement Checkbox
    terms_accepted = st.checkbox(
        "אני מאשר כי קראתי ואני מסכים לתקנון האתר ולהסכם הבוררות של Resolve AI",
        key="terms_claimant",
        value=st.session_state.terms_accepted_claimant
    )
    st.session_state.terms_accepted_claimant = terms_accepted

    # Show form only if terms accepted
    if terms_accepted:
        st.markdown("<br>", unsafe_allow_html=True)

        # Personal Details Form
        full_name = st.text_input(
            "שם מלא",
            key="claimant_full_name",
            placeholder="הזן שם פרטי ושם משפחה"
        )

        id_number = st.text_input(
            "מספר תעודת זהות / ח.ר",
            key="claimant_id",
            placeholder="הזן מספר תעודת זהות או מספר חברה"
        )

        email = st.text_input(
            "כתובת אימייל",
            key="claimant_email",
            placeholder="example@email.com"
        )

        phone = st.text_input(
            "מספר טלפון",
            key="claimant_phone",
            placeholder="05XXXXXXXX"
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("שמור והמשך", key="submit_claimant"):
                # Validation
                if not full_name or not id_number or not email or not phone:
                    st.error("נא למלא את כל השדות")
                else:
                    st.success("הפרטים נשמרו בהצלחה")
                    # Here you can save the data to database or session state
                    st.session_state.claimant_data = {
                        'full_name': full_name,
                        'id_number': id_number,
                        'email': email,
                        'phone': phone
                    }
    else:
        st.info("יש לאשר את התקנון והסכם הבוררות על מנת להמשיך")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# Page: Defendant Portal
# =====================================================
def render_defendant_portal():
    # Back Button
    st.markdown('<div class="back-button">', unsafe_allow_html=True)
    if st.button("חזרה לדף הבית", key="back_from_defendant"):
        go_to_home()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Portal Title
    st.markdown("""
        <h1 class="portal-title">מסוף נתבעים</h1>
    """, unsafe_allow_html=True)

    # Form Container
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # Section Title
    st.markdown("""
        <h2 class="section-title">רישום נתבע</h2>
    """, unsafe_allow_html=True)

    # Legal Agreement Checkbox
    terms_accepted = st.checkbox(
        "אני מאשר כי קראתי ואני מסכים לתקנון האתר ולהסכם הבוררות של Resolve AI",
        key="terms_defendant",
        value=st.session_state.terms_accepted_defendant
    )
    st.session_state.terms_accepted_defendant = terms_accepted

    # Show form only if terms accepted
    if terms_accepted:
        st.markdown("<br>", unsafe_allow_html=True)

        # Personal Details Form
        full_name = st.text_input(
            "שם מלא",
            key="defendant_full_name",
            placeholder="הזן שם פרטי ושם משפחה"
        )

        id_number = st.text_input(
            "מספר תעודת זהות / ח.ר",
            key="defendant_id",
            placeholder="הזן מספר תעודת זהות או מספר חברה"
        )

        email = st.text_input(
            "כתובת אימייל",
            key="defendant_email",
            placeholder="example@email.com"
        )

        phone = st.text_input(
            "מספר טלפון",
            key="defendant_phone",
            placeholder="05XXXXXXXX"
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("שמור והמשך", key="submit_defendant"):
                # Validation
                if not full_name or not id_number or not email or not phone:
                    st.error("נא למלא את כל השדות")
                else:
                    st.success("הפרטים נשמרו בהצלחה")
                    # Here you can save the data to database or session state
                    st.session_state.defendant_data = {
                        'full_name': full_name,
                        'id_number': id_number,
                        'email': email,
                        'phone': phone
                    }
    else:
        st.info("יש לאשר את התקנון והסכם הבוררות על מנת להמשיך")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# Main Application Router
# =====================================================
if st.session_state.page == 'home':
    render_home_page()
elif st.session_state.page == 'claimant_portal':
    render_claimant_portal()
elif st.session_state.page == 'defendant_portal':
    render_defendant_portal()
