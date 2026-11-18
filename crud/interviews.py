from database.db_utils import run_query, run_select


def save_interview_scores(student_id, communication_score, technical_score, aptitude_score):

    run_query(
        """
        INSERT INTO interviews
        (
            student_id,
            communication_score,
            technical_score,
            aptitude_score
        )
        VALUES
        (%s, %s, %s, %s)
        """,
        (
            student_id,
            communication_score,
            technical_score,
            aptitude_score,
        ),
    )


def get_interview_scores():

    return run_select(
        """
        SELECT

            i.interview_id,

            s.name,

            s.department,

            i.communication_score,

            i.technical_score,

            i.aptitude_score,

            ROUND(
                (
                    i.communication_score +
                    i.technical_score +
                    i.aptitude_score
                ) / 3,
                2
            ) AS average_score

        FROM interviews i

        JOIN students s

            ON i.student_id = s.student_id

        ORDER BY

            average_score DESC
        """
    )