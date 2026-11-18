import streamlit as st

from crud.students import get_student_options
from crud.skills import (
    save_skills,
    get_skill_summary,
)


st.header("Skills")


student_options = get_student_options()


if len(student_options) == 0:

    st.info("Add a student first.")

    st.stop()


selected_student = st.selectbox(

    "Student",

    list(student_options.keys())

)


skills = st.multiselect(

    "Skills",

    [

        "Python",
        "Java",
        "C++",
        "SQL",
        "Excel",
        "Power BI",
        "Tableau",
        "Data Structures",
        "Algorithms",
        "DBMS",
        "Operating Systems",
        "Computer Networks",
        "Web Development",
        "Cloud Computing",
        "Cyber Security",
        "Linux",
        "Data Analytics",
        "Data Science",
        "Data Visualization",
        "Machine Learning",
        "Deep Learning",
        "Generative AI",
        "TensorFlow",
        "PyTorch",
        "NLP",
        "Computer Vision",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Statistics",
        "Embedded Systems",
        "VLSI",
        "Digital Electronics",
        "Microcontrollers",
        "Arduino",
        "PCB Design",
        "Signal Processing",
        "Communication Systems",
        "MATLAB",
        "IoT",
        "Power Systems",
        "Electrical Machines",
        "PLC",
        "SCADA",
        "Power Electronics",
        "Control Systems",
        "Industrial Automation",
        "AutoCAD",
        "SolidWorks",
        "CATIA",
        "ANSYS",
        "CNC Programming",
        "Manufacturing",
        "Quality Control",
        "Thermodynamics",
        "Robotics",
        "STAAD Pro",
        "Revit",
        "ETABS",
        "Surveying",
        "Construction Management",
        "Quantity Estimation",
        "Structural Analysis",
        "Project Management"
    ]

)


if st.button("Save Skills"):

    save_skills(

        student_options[selected_student],

        skills

    )

    st.success("Skills Saved Successfully")

    st.rerun()


st.subheader("Skill Summary")

st.dataframe(

    get_skill_summary(),

    width="stretch",

    hide_index=True

)