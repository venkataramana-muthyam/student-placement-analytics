from database.connection import get_connection
from database.db_utils import run_query, run_select


def save_skills(student_id, selected_skills):

    run_query(
        "DELETE FROM skills WHERE student_id = %s",
        (student_id,)
    )

    connection = get_connection()

    cursor = connection.cursor()

    for skill in selected_skills:

        cursor.execute(
            """
            INSERT INTO skills
            (
                student_id,
                skill_name
            )
            VALUES
            (%s, %s)
            """,
            (
                student_id,
                skill
            )
        )

    connection.commit()

    cursor.close()

    connection.close()

def get_skill_summary():

    return run_select(

        """
        SELECT

            s.student_id,

            s.name,

            s.department,

            GROUP_CONCAT(

                k.skill_name

                ORDER BY k.skill_name

                SEPARATOR ', '

            ) AS skills

        FROM students s

        LEFT JOIN skills k

            ON s.student_id = k.student_id

        GROUP BY

            s.student_id,

            s.name,

            s.department

        ORDER BY

            s.student_id DESC
        """
    )