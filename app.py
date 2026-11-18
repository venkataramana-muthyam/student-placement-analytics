import streamlit as st

from database.connection import create_tables

st.set_page_config(
    page_title="Student Placement Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)


try:
    create_tables()

except Exception as error:

    st.error(f"MySQL Connection Error : {error}")

    st.stop()

st.title("🎓 Student Placement Analytics Dashboard")

st.write(
    "Analyze student placement performance, skills, interview scores and hiring trends."
)