import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="DevStart: Beginner Web Developer Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style to ensure full screen presentation
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none !important;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

html_file = Path(__file__).parent / "index.html"
if html_file.exists():
    html_code = html_file.read_text(encoding="utf-8")
    components.html(html_code, height=950, scrolling=True)
else:
    st.error("index.html not found.")
