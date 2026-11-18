import streamlit as st

from analytics.analytics import (
    get_department_analytics,
    get_department_ranking,
    get_top_skills
)


st.header("Analytics")


analytics = get_department_analytics()


if len(analytics) == 0:

    st.info("Add student and placement data to view analytics.")

else:

    st.subheader("Department Placement Summary")

    st.dataframe(

        analytics,

        width="stretch",

        hide_index=True

    )

    st.bar_chart(

        analytics,

        x="department",

        y="placed_students",

        width="stretch"

    )

st.divider()

st.subheader("Department Ranking")
ranking = get_department_ranking()

if len(ranking) > 0:

    st.dataframe(
        ranking,
        width="stretch",
        hide_index=True
    )

    for row in ranking:

        row["placement_rate"] = float(
            row["placement_rate"]
        )

    st.bar_chart(
        ranking,
        x="department",
        y="placement_rate",
        width="stretch"
    )

else:

    st.info(
        "No placement data available."
    )

st.divider()

st.subheader("Top Skills Analytics")

skills = get_top_skills()

if len(skills) > 0:

    st.dataframe(
        skills,
        width="stretch",
        hide_index=True
    )

    st.bar_chart(
        skills,
        x="skill_name",
        y="student_count",
        width="stretch"
    )

else:

    st.info(
        "No skills data available."
    )