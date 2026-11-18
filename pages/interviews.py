import streamlit as st

from crud.students import get_student_options
from crud.interviews import (
    save_interview_scores,
    get_interview_scores,
)


st.header("Interview Scores")


student_options = get_student_options()


if len(student_options) == 0:

    st.info("Add a student first.")

    st.stop()


selected_student = st.selectbox(

    "Student",

    list(student_options.keys())

)


communication_score = st.slider(

    "Communication",

    0,

    100

)

technical_score = st.slider(

    "Technical",

    0,

    100

)

aptitude_score = st.slider(

    "Aptitude",

    0,

    100

)


if st.button("Save Scores"):

    save_interview_scores(

        student_options[selected_student],

        communication_score,

        technical_score,

        aptitude_score

    )

    st.success("Interview Scores Saved Successfully")

    st.rerun()


st.subheader("Interview Results")

st.dataframe(

    get_interview_scores(),

    width="stretch",

    hide_index=True

)