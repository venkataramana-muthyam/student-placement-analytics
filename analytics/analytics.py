from database.db_utils import run_select


def get_dashboard_data():

    data = run_select(
        """
        SELECT
            (SELECT COUNT(*) FROM students WHERE is_deleted = FALSE) AS total_students,
            (SELECT COUNT(DISTINCT student_id) FROM placements) AS placed_students,
            (SELECT COALESCE(AVG(package_lpa), 0) FROM placements) AS avg_package
        """
    )[0]

    total_students = data["total_students"]

    placed_students = data["placed_students"]

    placement_rate = 0

    if total_students > 0:

        placement_rate = (
            placed_students / total_students
        ) * 100

    return (
        total_students,
        placed_students,
        placement_rate,
        data["avg_package"],
    )


def get_department_analytics():

    return run_select(
        """
        SELECT

            s.department,

            COUNT(DISTINCT s.student_id) AS total_students,

            COUNT(DISTINCT p.student_id) AS placed_students

        FROM students s

        LEFT JOIN placements p

            ON s.student_id = p.student_id
            WHERE s.is_deleted = FALSE

        GROUP BY

            s.department

        ORDER BY

            s.department
        """
    )

def calculate_readiness_score(
    cgpa,
    communication,
    technical,
    aptitude
):

    cgpa = float(cgpa)

    score = (

        (cgpa * 10 * 0.30)

        + (communication * 0.20)

        + (technical * 0.30)

        + (aptitude * 0.20)

    )

    return round(score, 2)

def get_readiness_students():

    return run_select(
        """
        SELECT

            s.name,

            s.cgpa,

            i.communication_score,

            i.technical_score,

            i.aptitude_score

        FROM students s

        JOIN interviews i

            ON s.student_id = i.student_id

        WHERE s.is_deleted = FALSE
        """
    )

def get_readiness_status(score):

    if score >= 80:

        return "High Chance"

    elif score >= 60:

        return "Medium Chance"

    else:

        return "Low Chance"
    

#  ----------- Department wise ranking-------------   
def get_department_ranking():

    return run_select(
        """
        SELECT

            s.department,

            COUNT(DISTINCT s.student_id) AS total_students,

            COUNT(DISTINCT p.student_id) AS placed_students,

            CAST(
                ROUND(
                    (
                        COUNT(DISTINCT p.student_id) * 100.0
                    ) /
                    COUNT(DISTINCT s.student_id),
                    2
                ) AS DOUBLE
            ) AS placement_rate

        FROM students s

        LEFT JOIN placements p

            ON s.student_id = p.student_id

        WHERE s.is_deleted = FALSE

        GROUP BY s.department

        ORDER BY placement_rate DESC
        """
    )

def get_top_skills():

    return run_select(
        """
        SELECT

            skill_name,

            COUNT(*) AS student_count

        FROM skills

        GROUP BY skill_name

        ORDER BY student_count DESC
        """
    )