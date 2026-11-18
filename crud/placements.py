from database.db_utils import run_query, run_select


def save_placement(student_id, company, package_lpa, placement_date):

    run_query(
        """
        INSERT INTO placements
        (
            student_id,
            company,
            package_lpa,
            placement_date
        )
        VALUES
        (%s, %s, %s, %s)
        """,
        (
            student_id,
            company,
            package_lpa,
            placement_date,
        ),
    )


def get_placements():

    return run_select(
        """
        SELECT

            p.placement_id,

            s.name,

            s.department,

            p.company,

            p.package_lpa,

            p.placement_date

        FROM placements p

        JOIN students s

            ON p.student_id = s.student_id

        ORDER BY

            p.placement_date DESC
        """
    )