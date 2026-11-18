import streamlit as st

from analytics.analytics import (
    get_dashboard_data,
    get_readiness_students,
    calculate_readiness_score,
    get_readiness_status
)
from crud.students import get_students


st.header("Dashboard")


total_students, placed_students, placement_rate, avg_package = get_dashboard_data()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Students",
        total_students
    )

with col2:
    st.metric(
        "Placed Students",
        placed_students
    )

with col3:
    st.metric(
        "Placement Rate",
        f"{placement_rate:.1f}%"
    )

with col4:
    st.metric(
        "Average Package",
        f"{float(avg_package):.2f} LPA"
    )


st.divider()

st.subheader("Recent Students")

students = get_students()

st.dataframe(
    students,
    width="stretch",
    hide_index=True
)

st.subheader("Placement Readiness Scores")

students = get_readiness_students()

if len(students) > 0:

    readiness_data = []

    for student in students:

        score = calculate_readiness_score(

            student["cgpa"],

            student["communication_score"],

            student["technical_score"],

            student["aptitude_score"]

        )

        readiness_data.append({

            "Student": student["name"],

            "Readiness Score (%)": score,

            "Status": get_readiness_status(score)

        })

    st.dataframe(

        readiness_data,

        width="stretch",

        hide_index=True

    )

else:

    st.info(
        "Add interview scores to view readiness scores."
    )