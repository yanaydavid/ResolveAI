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

    /* Message Display */
    .message-box {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid #DAA520;
        border-radius: 15px;
        padding: 30px;
        margin-top: 30px;
        color: white;
        font-size: 1.3rem;
        text-align: center;
        animation: fadeIn 0.5s ease;
        backdrop-filter: blur(10px);
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* RTL Columns */
    [data-testid="column"] {
        direction: rtl;
        text-align: center;
    }

    /* Mobile Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
            margin-bottom: 40px;
        }

        .column-title {
            font-size: 1.8rem;
        }

        .column-card {
            padding: 40px 20px;
            min-height: 300px;
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
if 'claimant_clicked' not in st.session_state:
    st.session_state.claimant_clicked = False
if 'defendant_clicked' not in st.session_state:
    st.session_state.defendant_clicked = False

# =====================================================
# Main Application
# =====================================================

# Main Title
st.markdown("""
    <div class="main-content">
        <h1 class="main-title">ברוכים הבאים ל-Resolve AI</h1>
    </div>
""", unsafe_allow_html=True)

# Two Columns Layout
col1, col2 = st.columns(2, gap="large")

# Right Column - Claimant (תובע)
with col1:
    st.markdown("""
        <div class="column-card">
            <h2 class="column-title">רוצה להגיש תביעה?</h2>
        </div>
    """, unsafe_allow_html=True)

    if st.button("לחץ כאן", key="claimant_button"):
        st.session_state.claimant_clicked = True
        st.session_state.defendant_clicked = False

    if st.session_state.claimant_clicked:
        st.markdown("""
            <div class="message-box">
                מעבר למסוף תובע...
            </div>
        """, unsafe_allow_html=True)

# Left Column - Defendant (נתבע)
with col2:
    st.markdown("""
        <div class="column-card">
            <h2 class="column-title">רוצה להגיש כתב הגנה?</h2>
        </div>
    """, unsafe_allow_html=True)

    if st.button("לחץ כאן", key="defendant_button"):
        st.session_state.defendant_clicked = True
        st.session_state.claimant_clicked = False

    if st.session_state.defendant_clicked:
        st.markdown("""
            <div class="message-box">
                מעבר למסוף נתבע...
            </div>
        """, unsafe_allow_html=True)
