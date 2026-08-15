import streamlit as st


st.set_page_config(page_title="RESILIA", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background: #FFF7D6;
            color: #3D2A1F;
        }

        h1 {
            color: #A61717;
            font-weight: 750;
            letter-spacing: 0.04em;
        }

        [data-testid="stCaptionContainer"] {
            color: #7A4130;
            font-size: 1.05rem;
        }

        [data-testid="stMarkdownContainer"] p {
            color: #3D2A1F;
            font-size: 1.05rem;
            line-height: 1.75;
        }

        .stButton > button {
            background-color: #B91C1C;
            border: 1px solid #B91C1C;
            border-radius: 8px;
            color: #FFFFFF;
            font-weight: 650;
            min-height: 46px;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            background-color: #8F1515;
            border-color: #8F1515;
            color: #FFFFFF;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("RESILIA")
st.caption("*An AI powered building maintenance and resilience system.*")

st.write(
    "RESILIA is an AI-powered building maintenance and resilience system that "
    "assesses structural stability and management performance across commercial "
    "and residential properties. By integrating aerial imagery, AI-driven computer "
    "vision, NLP, and machine learning with resident feedback, targeted CCTV "
    "monitoring, historical maintenance data, and appropriate sensors, RESILIA "
    "generates a dynamic Building Resilience & Maintenance Index for each property. "
    "This cost-effective, time-efficient, and future-ready solution leverages "
    "advanced ML and deep learning models to continuously evaluate building "
    "resilience, prioritize maintenance actions, and support more sustainable, "
    "data-driven facility management."
)

maintenance_col, feedback_col = st.columns(2)

with maintenance_col:
    if st.button("Maintanence", use_container_width=True):
        st.info("Maintanence dashboard selected.")

with feedback_col:
    if st.button("Feedback", use_container_width=True):
        st.info("Feedback portal selected.")
