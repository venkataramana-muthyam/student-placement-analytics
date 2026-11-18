
import streamlit as st
import pandas as pd
st.write("Students Page Loaded")
from crud.students import (
    add_student,
    get_students,
    get_student_options,
    delete_student,
    get_deleted_students,
    restore_student,
    permanent_delete_student,
    update_student,
    get_student_by_id
)

st.header("Student Management")


with st.form("student_form"):

    name = st.text_input("Student Name")

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )

    department = st.selectbox(
        "Department",
        [
            "CSE",
            "ECE",
            "EEE",
            "IT",
            "CSE-AIML",
            "CSE-DS",
            "MECH",
            "CIVIL",
            "CSE-IOT"
        ]
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    graduation_year = st.number_input(
        "Graduation Year",
        min_value=2024,
        max_value=2035
    )

    submit = st.form_submit_button("Add Student")


    if submit:

        if name.strip() == "":

            st.error("Student name is required.")

        else:

            add_student(
                name.strip(),
                gender,
                department,
                cgpa,
                graduation_year
            )

            st.success("Student Added Successfully")

            st.rerun()


st.subheader("All Students")

search_text = st.text_input(
    "Search Student By Name"
)

students = get_students()

if search_text:

    students = [

        student

        for student in students

        if search_text.lower()

        in student["name"].lower()

    ]


st.dataframe(
    students,
    width="stretch",
    hide_index=True
)

if len(students) > 0:

    csv = pd.DataFrame(
        students
    ).to_csv(
        index=False
    )

    st.download_button(

        label="Download Students CSV",

        data=csv,

        file_name="students.csv",

        mime="text/csv"

    )


st.divider()

st.subheader("Delete Student")

student_options = get_student_options()

if len(student_options) > 0:

    selected_student = st.selectbox(
        "Select Student To Delete",
        list(student_options.keys())
    )

    if st.button("Delete Student"):

        delete_student(
            student_options[selected_student]
        )

        st.success(
            "Student Deleted Successfully"
        )

        st.rerun()

st.divider()

st.subheader("Deleted Students History")

deleted_students = get_deleted_students()

if len(deleted_students) > 0:

    st.dataframe(
        deleted_students,
        width="stretch"
    )

    restore_options = {

        f"{student['student_id']} - {student['name']}":
        student['student_id']

        for student in deleted_students

    }

    selected_restore_student = st.selectbox(

        "Select Student To Restore",

        list(restore_options.keys())

    )

    if st.button("Restore Student"):

        restore_student(

            restore_options[selected_restore_student]

        )

        st.success(

            "Student Restored Successfully"

        )

        st.rerun()

    if st.button("Permanent Delete"):

        permanent_delete_student(

            restore_options[selected_restore_student]

        )

        st.success(

            "Student Permanently Deleted"

        )

        st.rerun()

else:

    st.info("No Deleted Students Found")

st.divider()

st.subheader("Update Student")

student_options = get_student_options()

if len(student_options) > 0:

    selected_student = st.selectbox(

        "Select Student To Update",

        list(student_options.keys())

    )

    student_id = student_options[selected_student]

    student = get_student_by_id(student_id)

    update_name = st.text_input(
        "Update Name",
        value=student["name"]
    )

    update_gender = st.selectbox(
        "Update Gender",
        ["Male", "Female"],
        index=0 if student["gender"] == "Male" else 1
    )

    departments = [
        "CSE",
        "ECE",
        "EEE",
        "IT",
        "CSE-AIML",
        "CSE-DS",
        "MECH",
        "CIVIL",
        "CSE-IOT"
    ]

    update_department = st.selectbox(
        "Update Department",
        departments,
        index=departments.index(student["department"])
    )

    update_cgpa = st.number_input(
        "Update CGPA",
        min_value=0.0,
        max_value=10.0,
        value=float(student["cgpa"])
    )

    update_year = st.number_input(
        "Update Graduation Year",
        min_value=2024,
        max_value=2035,
        value=int(student["graduation_year"])
    )

    if st.button("Update Student"):

        update_student(

            student_id,

            update_name,

            update_gender,

            update_department,

            update_cgpa,

            update_year

        )

        st.success(
            "Student Updated Successfully"
        )

        st.rerun()

else:

    st.info("No Students Available")