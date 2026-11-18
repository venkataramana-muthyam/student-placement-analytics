import streamlit as st

from crud.students import get_student_options
from crud.placements import (
    save_placement,
    get_placements,
)


st.header("Placements")


student_options = get_student_options()


if len(student_options) == 0:

    st.info("Add a student first.")

    st.stop()


selected_student = st.selectbox(

    "Student",

    list(student_options.keys())

)


company = st.text_input(

    "Company Name"

)

package_lpa = st.number_input(

    "Package LPA",

    min_value=0.0,

    step=0.1

)

placement_date = st.date_input(

    "Placement Date"

)


if st.button("Save Placement"):

    if company.strip() == "":

        st.error("Company name is required.")

    else:

        save_placement(

            student_options[selected_student],

            company.strip(),

            package_lpa,

            placement_date

        )

        st.success("Placement Saved Successfully")

        st.rerun()


st.subheader("Placement Records")

st.dataframe(

    get_placements(),

    width="stretch",

    hide_index=True

)