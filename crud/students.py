from database.db_utils import run_query, run_select


def add_student(name, gender, department, cgpa, graduation_year):

    run_query(
        """
        INSERT INTO students
        (
            name,
            gender,
            department,
            cgpa,
            graduation_year
        )
        VALUES
        (%s, %s, %s, %s, %s)
        """,
        (
            name,
            gender,
            department,
            cgpa,
            graduation_year,
        ),
    )


def get_students():

    return run_select(
        """
        SELECT
            student_id,
            name,
            gender,
            department,
            cgpa,
            graduation_year
        FROM students

        WHERE is_deleted = FALSE

        ORDER BY student_id DESC
        """
    )

def get_student_options():

    students = get_students()

    return {

        f"{student['student_id']} - {student['name']}": student["student_id"]

        for student in students

    }
def delete_student(student_id):

    run_query(
        """
        UPDATE students

        SET is_deleted = TRUE

        WHERE student_id = %s
        """,
        (student_id,)
    )

def get_deleted_students():

    return run_select(
        """
        SELECT *

        FROM students

        WHERE is_deleted = TRUE

        ORDER BY student_id DESC
        """
    )


def restore_student(student_id):

    run_query(
        """
        UPDATE students

        SET is_deleted = FALSE

        WHERE student_id = %s
        """,
        (student_id,)
    )

def permanent_delete_student(student_id):

    run_query(
        """
        DELETE FROM students

        WHERE student_id = %s
        """,
        (student_id,)
    )

def update_student(
    student_id,
    name,
    gender,
    department,
    cgpa,
    graduation_year
):

    run_query(
        """
        UPDATE students

        SET
            name = %s,
            gender = %s,
            department = %s,
            cgpa = %s,
            graduation_year = %s

        WHERE student_id = %s
        """,
        (
            name,
            gender,
            department,
            cgpa,
            graduation_year,
            student_id
        )
    )

def get_student_by_id(student_id):

    result = run_select(
        """
        SELECT *

        FROM students

        WHERE student_id = %s
        """,
        (student_id,)
    )

    if len(result) > 0:

        return result[0]

    return None

