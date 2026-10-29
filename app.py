from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Practice Hub: GK, Grammar and English",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own chrome so the app fills the page.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "practice_hub.html").read_text(encoding="utf-8")

# The app scrolls inside this frame. Increase height if you want a taller view.
components.html(html, height=1600, scrolling=True)
